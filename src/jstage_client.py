from __future__ import annotations

import logging
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

import requests

from src.config import jst_today
from src.models import Article, NA

LOG = logging.getLogger(__name__)
ENDPOINT = "https://api.jstage.jst.go.jp/searchapi/do"
HEADERS = {"User-Agent": "JapaneseCriticalCareLiteratureCollector/1.0 (GitHub Actions)"}
NS = {"a": "http://www.w3.org/2005/Atom", "p": "http://prismstandard.org/namespaces/basic/2.0/"}


def _text(node: ET.Element, paths: list[str], default: str = NA) -> str:
    for path in paths:
        found = node.find(path, NS)
        if found is not None and found.text and found.text.strip():
            return found.text.strip()
    return default


def _request(session: requests.Session, params: dict[str, str | int], retries: int = 3) -> bytes:
    for attempt in range(retries):
        try:
            response = session.get(ENDPOINT, params=params, headers=HEADERS, timeout=20)
            response.raise_for_status()
            return response.content
        except (requests.RequestException, TimeoutError):
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    return b""


def parse_jstage(xml: bytes, retrieved_at: str) -> list[Article]:
    root = ET.fromstring(xml)
    articles = []
    for entry in root.findall("a:entry", NS):
        title_ja = _text(entry, ["a:article_title/a:ja", "a:title"])
        title_en = _text(entry, ["a:article_title/a:en"])
        url = _text(entry, ["a:article_link/a:ja", "a:id"])
        if url == NA:
            link = entry.find("a:link", NS)
            url = link.get("href", NA) if link is not None else NA
        doi = _text(entry, ["p:doi"])
        authors = []
        for author in entry.findall("a:author", NS):
            name = _text(author, ["a:ja/a:name", "a:en/a:name"], "")
            if name:
                authors.append(name)
        online = _text(entry, ["a:updated"])
        abstract_ja = _text(entry, ["a:abstract/a:ja", "a:summary/a:ja", "a:summary"], "日本語抄録なし")
        abstract_en = _text(entry, ["a:abstract/a:en"], NA)
        parts = urlparse(url).path.strip("/").split("/") if url != NA else []
        article_id = f"{parts[1]}/{parts[4]}" if len(parts) > 5 and parts[0] == "article" else NA
        articles.append(Article(
            article_key=(f"doi:{doi.casefold()}" if doi != NA else f"jstage:{article_id}"),
            jstage_article_id=article_id, doi=doi, title_ja=title_ja, title_en=title_en, authors=authors,
            journal=_text(entry, ["a:material_title/a:ja", "a:material_title/a:en"]),
            issn=_text(entry, ["p:eIssn", "p:issn"]), volume=_text(entry, ["p:volume"]),
            issue=_text(entry, ["p:number"]), start_page=_text(entry, ["p:startingPage"]),
            end_page=_text(entry, ["p:endingPage"]), publication_year=_text(entry, ["a:pubyear"]),
            online_date=online, updated_date=online, source_databases=["J-STAGE"], jstage_url=url,
            abstract_ja=abstract_ja, abstract_en=abstract_en,
            doi_url=(f"https://doi.org/{doi}" if doi != NA else NA), html_url=url,
            free_full_text=False, retrieved_at=retrieved_at,
        ))
    return articles


def search(groups: dict[str, list[str]], days_back: int = 7, interval: float = 1.0,
           session: requests.Session | None = None) -> list[Article]:
    session = session or requests.Session()
    now = datetime.now(timezone.utc)
    today = jst_today()
    year = (today - timedelta(days=days_back)).year
    found: list[Article] = []
    for words in groups.values():
        # APIでは同一項目内の空白はANDになるため、代表語を個別検索する。
        for word in words[:2]:
            try:
                xml = _request(session, {"service": 3, "article": word, "pubyearfrom": year,
                                         "pubyearto": today.year, "count": 20})
                found.extend(parse_jstage(xml, now.isoformat()))
            except (requests.RequestException, ET.ParseError) as exc:
                LOG.warning("J-STAGE検索を継続できない語がありました (%s): %s", word, exc)
            time.sleep(interval)
    return found
