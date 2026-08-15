from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import Any

import requests

from src.models import Article, NA

LOG = logging.getLogger(__name__)
ENDPOINT = "https://cir.nii.ac.jp/opensearch/articles"
HEADERS = {"User-Agent": "JapaneseCriticalCareLiteratureCollector/1.0 (GitHub Actions)"}


def _value(item: dict[str, Any], key: str, default: str = NA) -> str:
    value = item.get(key, default)
    if isinstance(value, list):
        value = value[0] if value else default
    if isinstance(value, dict):
        value = value.get("@value") or value.get("@id") or default
    return str(value).strip() or default


def _list(item: dict[str, Any], key: str) -> list[str]:
    value = item.get(key, [])
    value = value if isinstance(value, list) else [value]
    return [str(v.get("@value", v) if isinstance(v, dict) else v) for v in value if v]


def parse_cinii(payload: dict[str, Any], retrieved_at: str) -> list[Article]:
    articles = []
    for item in payload.get("items", []):
        url = _value(item, "@id")
        cinii_id = url.rstrip("/").split("/")[-1] if url != NA else NA
        doi = _value(item, "prism:doi")
        title = _value(item, "title")
        descriptions = _list(item, "dc:description")
        abstract = descriptions[0] if descriptions else "日本語抄録なし"
        date_value = _value(item, "prism:publicationDate")
        articles.append(Article(
            article_key=(f"doi:{doi.casefold()}" if doi != NA else f"cinii:{cinii_id}"),
            cinii_id=cinii_id, doi=doi, title_ja=title, authors=_list(item, "dc:creator"),
            journal=_value(item, "prism:publicationName"), issn=_value(item, "prism:issn"),
            volume=_value(item, "prism:volume"), issue=_value(item, "prism:number"),
            start_page=_value(item, "prism:startingPage"), end_page=_value(item, "prism:endingPage"),
            publication_year=(date_value[:4] if date_value != NA else NA), publication_date=date_value,
            article_type=_value(item, "dc:type"), source_databases=["CiNii Research"], cinii_url=url,
            abstract_ja=abstract, keywords=_list(item, "dc:subject"),
            doi_url=(f"https://doi.org/{doi}" if doi != NA else NA), retrieved_at=retrieved_at,
        ))
    return articles


def search(groups: dict[str, list[str]], app_id: str, interval: float = 1.0,
           session: requests.Session | None = None) -> list[Article]:
    session = session or requests.Session()
    found: list[Article] = []
    for words in groups.values():
        query = " OR ".join(words[:3])
        for attempt in range(3):
            try:
                response = session.get(ENDPOINT, params={"q": query, "count": 20, "sortorder": 0,
                                       "format": "json", "lang": "ja", "appid": app_id},
                                       headers=HEADERS, timeout=20)
                response.raise_for_status()
                found.extend(parse_cinii(response.json(), datetime.now(timezone.utc).isoformat()))
                break
            except (requests.RequestException, ValueError) as exc:
                if attempt == 2:
                    LOG.warning("CiNii Research検索を継続できない領域がありました: %s", exc)
                else:
                    time.sleep(2 ** attempt)
        time.sleep(interval)
    return found
