from __future__ import annotations

import logging
import re
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import requests
from pypdf import PdfReader
from pypdf.errors import PyPdfError

from src.content_analyzer import analyze_fulltext
from src.models import Article, NA

LOG = logging.getLogger(__name__)
HEADERS = {"User-Agent": "JapaneseCriticalCareLiteratureCollector/1.0 (non-commercial research; bounded PDF review)"}


def official_jstage_pdf_url(article: Article) -> str | None:
    """既知のJ-STAGE論文URLから同一記事の公式PDF URLだけを構成する。"""
    url = article.jstage_url
    if not url.startswith("https://www.jstage.jst.go.jp/article/") or "/_article/" not in url:
        return None
    return url.replace("/_article/", "/_pdf/", 1)


def download_pdf(url: str, destination: Path, max_bytes: int,
                 session: requests.Session | None = None) -> None:
    session = session or requests.Session()
    with session.get(url, headers=HEADERS, timeout=30, stream=True, allow_redirects=True) as response:
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "").casefold()
        if "pdf" not in content_type:
            raise ValueError("公式URLからPDF以外が返されました")
        declared = int(response.headers.get("Content-Length", "0") or 0)
        if declared > max_bytes:
            raise ValueError("PDFが容量上限を超えています")
        size = 0
        with destination.open("wb") as stream:
            for chunk in response.iter_content(64 * 1024):
                if not chunk:
                    continue
                size += len(chunk)
                if size > max_bytes:
                    raise ValueError("PDFが容量上限を超えています")
                stream.write(chunk)
        if size < 5 or destination.read_bytes()[:5] != b"%PDF-":
            raise ValueError("有効なPDFを確認できません")


def extract_pdf_text(path: Path, max_pages: int = 100) -> str:
    reader = PdfReader(str(path))
    if reader.is_encrypted:
        raise ValueError("暗号化PDFは解析しません")
    pages = []
    for page in reader.pages[:max_pages]:
        value = page.extract_text() or ""
        if value.strip():
            pages.append(value)
    text = re.sub(r"[ \t]+", " ", "\n".join(pages))
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def review_pdf_backlog(articles: list[Article], limit: int = 3, max_bytes: int = 20 * 1024 * 1024,
                       interval: float = 10.0, session: requests.Session | None = None) -> list[Article]:
    """未確認文献を少数ずつ処理する。PDF本体は一時ファイルから永続保存しない。"""
    if limit <= 0:
        return []
    reviewed: list[Article] = []
    attempted = 0
    session = session or requests.Session()
    for article in articles:
        if attempted >= limit or article.fulltext_reviewed or article.pdf_review_status != "未確認":
            continue
        url = official_jstage_pdf_url(article)
        if not url:
            article.pdf_review_status = "対象外"
            continue
        attempted += 1
        article.pdf_checked_at = datetime.now(timezone.utc).isoformat()
        try:
            with tempfile.TemporaryDirectory(prefix="literature-pdf-") as directory:
                path = Path(directory) / "article.pdf"
                download_pdf(url, path, max_bytes, session)
                text = extract_pdf_text(path)
            article.pdf_url = url
            if len(text) < 200:
                raise ValueError("PDF本文を十分に抽出できません")
            analyze_fulltext(article, text)
            article.pdf_review_status = "本文解析済み"
            article.fulltext_character_count = len(text)
        except (requests.RequestException, ValueError, OSError, PyPdfError) as exc:
            article.pdf_review_status = "PDF取得・解析不可"
            LOG.warning("PDFを解析できませんでした (%s): %s", article.article_key, exc)
        reviewed.append(article)
        if attempted < limit:
            time.sleep(interval)
    return reviewed
