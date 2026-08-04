from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

JST = ZoneInfo("Asia/Tokyo")


def jst_today(now: datetime | None = None) -> date:
    """GitHub ActionsのUTC環境でも日本時間の日付を返す。"""
    instant = now or datetime.now(timezone.utc)
    if instant.tzinfo is None:
        instant = instant.replace(tzinfo=timezone.utc)
    return instant.astimezone(JST).date()

SEARCH_GROUPS = {
    "集中治療": ["集中治療", "集中治療室", "ICU", "クリティカルケア", "重症患者"],
    "救急看護": ["救急医療", "救急看護", "救命救急", "救急外来", "トリアージ"],
    "呼吸管理": ["人工呼吸", "呼吸管理", "NPPV", "HFNC", "ARDS"],
    "鎮痛・鎮静・せん妄": ["疼痛", "鎮痛", "鎮静", "せん妄", "CAM-ICU"],
    "敗血症・感染": ["敗血症", "感染管理", "VAP", "CLABSI"],
    "蘇生・循環管理": ["循環管理", "心停止", "心肺蘇生", "蘇生後管理"],
    "ECMO": ["ECMO", "ECPR"],
    "外傷": ["多発外傷", "重症外傷", "出血性ショック", "大量輸血"],
    "神経集中治療": ["頭部外傷", "TBI", "くも膜下出血", "神経集中治療"],
    "病院前救護": ["フライトナース", "ドクターヘリ", "病院前救護", "救急救命士"],
    "看護・安全・倫理": ["看護教育", "医療安全", "家族看護", "倫理", "終末期看護"],
}


def _bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Config:
    root: Path
    cinii_app_id: str | None
    max_articles: int = 20
    dry_run: bool = False
    enable_cinii: bool = True
    enable_pubmed_japanese: bool = False
    days_back: int = 7
    request_interval: float = 1.0

    @classmethod
    def from_env(cls, root: Path | None = None) -> "Config":
        load_dotenv()
        value = max(1, min(100, int(os.getenv("MAX_ARTICLES", "20"))))
        days = max(1, min(3650, int(os.getenv("DAYS_BACK", "7"))))
        return cls(
            root=(root or Path.cwd()).resolve(),
            cinii_app_id=os.getenv("CINII_APP_ID") or None,
            max_articles=value,
            days_back=days,
            dry_run=_bool("DRY_RUN", False),
            enable_cinii=_bool("ENABLE_CINII", True),
            enable_pubmed_japanese=_bool("ENABLE_PUBMED_JAPANESE", False),
        )
