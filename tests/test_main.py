from datetime import date, datetime, timezone

from src.config import Config
from src.config import jst_today
from src.main import collect, run
from src.models import Article


def test_no_cinii_id_runs_jstage_only(monkeypatch, tmp_path):
    called = {"cinii": False}
    monkeypatch.setattr("src.main.jstage_client.search", lambda *a, **k: [])
    monkeypatch.setattr("src.main.cinii_client.search", lambda *a, **k: called.update(cinii=True))
    config = Config(root=tmp_path, cinii_app_id=None, request_interval=0)
    assert collect(config) == []
    assert called["cinii"] is False


def test_no_new_articles_creates_no_files(monkeypatch, tmp_path):
    monkeypatch.setattr("src.main.collect", lambda config: [])
    assert run(Config(root=tmp_path, cinii_app_id=None)) == 0
    assert not (tmp_path / "literature").exists()


def test_dry_run_writes_nothing(monkeypatch, tmp_path):
    monkeypatch.setattr("src.main.collect", lambda config: [Article(article_key="x")])
    assert run(Config(root=tmp_path, cinii_app_id=None, dry_run=True)) == 1
    assert list(tmp_path.iterdir()) == []


def test_jst_date_after_utc_day_boundary():
    instant = datetime(2026, 8, 4, 22, 30, tzinfo=timezone.utc)
    assert str(jst_today(instant)) == "2026-08-05"


def test_days_back_from_environment(monkeypatch, tmp_path):
    monkeypatch.delenv("START_YEAR", raising=False)
    monkeypatch.setenv("DAYS_BACK", "365")
    assert Config.from_env(tmp_path).days_back == 365


def test_start_year_overrides_days_back(monkeypatch, tmp_path):
    monkeypatch.setenv("START_YEAR", "2020")
    monkeypatch.setenv("DAYS_BACK", "7")
    expected = (jst_today() - date(2020, 1, 1)).days + 1
    assert Config.from_env(tmp_path).days_back == expected
