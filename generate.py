#!/usr/bin/fontforge

import fontforge
import psMat

CODEPOINTS = [
  0x2022,  # •
  0x21E7,  # ⇧ (macOS Shift key)
  0x2300,  # ⌀
  0x2303,  # ⌃ (macOS Control key)
  0x2318,  # ⌘ (macOS Command key)
  0x2325,  # ⌥ (macOS Option key)
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

SUBSTITUTES = [
  'source/NotoSansMath-Regular.ttf',
  'source/NotoSansSymbols-Regular.ttf',
  'source/NotoSansSymbols2-Regular.ttf',
]

###

subs = [fontforge.open(s) for s in SUBSTITUTES]

def _copy_from_subs(cp):
  for s in subs:
    if cp in s:
      s.selection.select(cp)
      s.copy()
      return
  raise Exception(f"Glyph 0x{cp:04x} not found in any font.")


for f in FONTS:
  font = fontforge.open('source/' + f['file'])
  for cp in CODEPOINTS:
    if not cp in font:
      _copy_from_subs(cp)
      font.selection.select(cp)
      font.paste()
      glyph = font[cp]
      if f['weight']:
        glyph.changeWeight(f['weight'])
      if f['skew']:
        glyph.transform(psMat.skew(f['skew']))
  font.generate(f['file'])
