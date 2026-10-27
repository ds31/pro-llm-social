# pro-llm-social

Карусели Instagram [@pro_llm](https://www.instagram.com/pro_llm/) к разборам [pro-llm.ru](https://pro-llm.ru). Пакеты с кодом разборов — в [pro-llm-razbory](https://github.com/ds31/pro-llm-razbory).

Слайд — `<section class="slide">` в HTML, 1080×1350. Палитра и шрифты — как на сайте.

```
template/          стили, шрифты (OFL), аватар
razbor-01/         slides.html → slide-01.png … slide-08.png
news/nNN-<тема>/    карусели «Новость + что это значит» из Telegram @pro_llm: slides.html, caption.md, PNG
reels/rNN-<тема>/   вертикальные ролики 1080×1920: mp4, подпись, credits.json (лицензии снимков в кадре)
render.py          HTML → PNG через Playwright и Chrome
```

Собрать слайды:

```bash
uv run --with playwright python render.py razbor-01/slides.html
```

Шрифты Onest, JetBrains Mono и Caveat распространяются по SIL Open Font License 1.1 — тексты лицензий в `template/fonts/`.

Контакт: asalhanvip@gmail.com
