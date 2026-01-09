#!/usr/bin/fontforge

import fontforge

CODEPOINTS = [
  0x2022,  # •
  0x2300,  # ⌀
  0x232B,  # ⌫
  0x23CE,  # ⏎
  0x2423,  # ␣
  0x25B8,  # ▸
  0x25BA,  # ►
  0x25BC,  # ▼
  0x2937,  # ⤷
]

FONTS = [
  dict(file='NotoSans-Light.ttf', weight=-30, skew=0),
  dict(file='NotoSans-LightItalic.ttf', weight=-30, skew=0.2),
  dict(file='NotoSans-Regular.ttf', weight=0, skew=0),
  dict(file='NotoSans-Italic.ttf', weight=0, skew=0.2),
  dict(file='NotoSans-Bold.ttf', weight=50, skew=0),
  dict(file='NotoSans-BoldItalic.ttf', weight=50, skew=0.2),
]

SUBSTITUTE = 'source/NotoSansMath-Regular.ttf'

subs = fontforge.open(SUBSTITUTE)
for f in FONTS:
  font = fontforge.open('source/' + f['file'])
  for cp in CODEPOINTS:
    if not cp in font or True:
      subs.selection.select(cp)
      subs.copy()
      font.selection.select(cp)
      font.paste()
      glyph = font[cp]
      if f['weight']:
        glyph.changeWeight(f['weight'])
      if f['skew']:
        glyph.transform(psMat.skew(f['skew']))
  font.generate(f['file'])
