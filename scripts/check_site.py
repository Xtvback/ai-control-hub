#!/usr/bin/env python3
"""Dependency-free static site sanity checks."""
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

class Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.has_title = False
        self.lang = None

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "html":
            self.lang = data.get("lang")
        if tag == "title":
            self.has_title = True
        if tag == "link" and data.get("rel") == "stylesheet":
            self.links.append(data.get("href"))

def check(site=SITE):
    page = site / "index.html"
    if not page.is_file():
        raise ValueError("Missing index.html")
    html = page.read_text(encoding="utf-8")
    parser = Checker()
    parser.feed(html)
    if parser.lang != "pt-PT" or not parser.has_title:
        raise ValueError("Missing Portuguese language or page title")
    if not parser.links:
        raise ValueError("Missing stylesheet reference")
    for link in parser.links:
        if not link or link.startswith(("/", "http:", "https:")) or ".." in Path(link).parts:
            raise ValueError("Stylesheet must be a safe relative path")
        if not (site / link).is_file():
            raise ValueError(f"Missing stylesheet: {link}")
    return True

if __name__ == "__main__":
    check()
    print("Static site checks passed")
