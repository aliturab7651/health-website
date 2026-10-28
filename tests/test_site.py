from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"


def read_index():
    return (SITE / "index.html").read_text(encoding="utf-8")


def test_files_exist():
    assert (SITE / "index.html").exists()
    assert (SITE / "style.css").exists()


def test_has_title():
    assert "<title>" in read_index()


def test_has_services_and_contact():
    html = read_index()
    assert 'id="services"' in html
    assert 'id="contact"' in html


def test_has_disclaimer():
    assert "doctor" in read_index().lower()
