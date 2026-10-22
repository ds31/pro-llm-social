"""Рендер карусели: каждый <section class="slide"> из slides.html → PNG 1080×1350 рядом с ним.

    uv run --with playwright python render.py razbor-01/slides.html
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def render(html: Path) -> list[Path]:
    files = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto(html.resolve().as_uri())
        page.evaluate("document.fonts.ready")
        slides = page.locator("section.slide")
        for i in range(slides.count()):
            f = html.parent / f"slide-{i + 1:02d}.png"
            slides.nth(i).screenshot(path=str(f))
            files.append(f)
        browser.close()
    return files


if __name__ == "__main__":
    for f in render(Path(sys.argv[1])):
        print(f)
