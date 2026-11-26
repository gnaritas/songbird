#!/usr/bin/env python3
"""make_og.py — og.png 1200x630 for Songbird demo host (t_fbffb777).
Lane painter pattern (v2 discipline from marisol 2026-11-26): hard text column
— every measured line must end <= TEXT_RIGHT — all art geometry >= ART_LEFT,
asserted before save. Dusk palette: night plum ground, amber sun, cream moon,
cream songbird on the horizon singing toward the Resy pill."""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public", "og.png")
W, H = 1200, 630
TEXT_RIGHT = 782
ART_LEFT = 838
fails = []

NIGHT  = (36, 31, 49)     # dusk ground
NIGHT2 = (46, 38, 62)     # depth band
WARM   = (62, 46, 46)     # warm dusk wedge
CREAM  = (250, 243, 230)
SUN    = (223, 160, 78)
CORAL  = (206, 105, 74)
CORAL2 = (178, 96, 74)
INK    = (26, 21, 34)

def F(size, bold=False):
    cands = (["/System/Library/Fonts/Supplemental/Iowan Old Style Bold.ttf",
              "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"] if bold else
             ["/System/Library/Fonts/Supplemental/Iowan Old Style Roman.ttf",
              "/System/Library/Fonts/Supplemental/Times New Roman.ttf"])
    for c in cands:
        if os.path.exists(c):
            try: return ImageFont.truetype(c, size)
            except OSError: pass
    return ImageFont.load_default()

def SANS(size, bold=False):
    cands = (["/System/Library/Fonts/Supplemental/Futura Bold.ttc", "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
              "/System/Library/Fonts/Arial Bold.ttf"] if bold else
             ["/System/Library/Fonts/Supplemental/Futura.ttc", "/System/Library/Fonts/Supplemental/Arial.ttf",
              "/System/Library/Fonts/Arial.ttf"])
    for c in cands:
        if os.path.exists(c):
            try: return ImageFont.truetype(c, size)
            except OSError: pass
    return ImageFont.load_default()

def MONO(size):
    for c in ["/System/Library/Fonts/Menlo.ttc", "/System/Library/Fonts/Monaco.ttf"]:
        if os.path.exists(c):
            try: return ImageFont.truetype(c, size)
            except OSError: pass
    return ImageFont.load_default()

img = Image.new("RGB", (W, H), NIGHT)
ov = Image.new("RGB", (W, H), NIGHT)
od = ImageDraw.Draw(ov)
od.rounded_rectangle([-240, 400, 720, 780], radius=200, fill=WARM)
od.rounded_rectangle([1020, -170, W + 60, 300], radius=180, fill=NIGHT2)
img = Image.blend(img, ov, 0.55)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 6], fill=SUN)
d.rectangle([0, H - 6, W, H], fill=SUN)

LX = 72

def put_tracked(text, f, x, y, fill, tracking, label):
    widths = [d.textlength(ch, font=f) for ch in text]
    tw = sum(widths) + tracking * (len(text) - 1)
    if x + tw > TEXT_RIGHT: fails.append(f"{label}: right {x + tw:.0f} > {TEXT_RIGHT}")
    cx = x
    for ch, cw in zip(text, widths):
        d.text((cx, y), ch, font=f, fill=fill, anchor="lm")
        cx += cw + tracking
    return tw

def put(text, f, x, y, fill, label):
    w = d.textlength(text, font=f)
    if x + w > TEXT_RIGHT: fails.append(f"{label}: right {x + w:.0f} > {TEXT_RIGHT}")
    d.text((x, y), text, font=f, fill=fill)
    return w

put_tracked("EAST END MARKET · RALEIGH, NC", MONO(19), LX, 104, SUN, 3, "kick")

h1 = F(70, True)
t1, t2 = "Daylight to dusk.", "Coffee to cocktails."
w1, w2 = d.textlength(t1, font=h1), d.textlength(t2, font=h1)
if max(w1, w2) > TEXT_RIGHT - LX: fails.append(f"h1: width {max(w1, w2):.0f} > {TEXT_RIGHT - LX}")
d.text((LX, 148), t1, font=h1, fill=CREAM)
d.text((LX, 234), t2, font=h1, fill=(222, 122, 92))

sub = SANS(22, True)
s1 = "Mornings: coffee, juice, tea — 8 AM–2 PM daily"
s2 = "Evenings: cocktails, wine, and dinner till midnight"
w1s, w2s = d.textlength(s1, font=sub), d.textlength(s2, font=sub)
if max(w1s, w2s) > TEXT_RIGHT - LX: fails.append(f"sub: width {max(w1s, w2s):.0f} > {TEXT_RIGHT - LX}")
mut = (CREAM[0] - 26, CREAM[1] - 26, CREAM[2] - 30)
d.text((LX, 344), s1, font=sub, fill=mut)
d.text((LX, 382), s2, font=sub, fill=mut)

def put_stub(text, f, x, y, fillbg, fillfg, pad, label):
    tw = d.textlength(text, font=f)
    bb = d.textbbox((x + pad, y), text, font=f, anchor="lm")
    box = [x, bb[1] - 11, x + tw + 2 * pad, bb[3] + 11]
    if box[2] > TEXT_RIGHT: fails.append(f"{label}: right {box[2]} > {TEXT_RIGHT}")
    d.rounded_rectangle(box, radius=(box[3] - box[1]) // 2, fill=fillbg)
    d.text((x + pad, y), text, font=f, fill=fillfg, anchor="lm")
put_stub("EVENING TABLES ON RESY", SANS(19, True), LX, 456, CORAL, (255, 252, 246), 16, "stub")

foot = SANS(21)
ft = "1020 E Whitaker Mill Rd, Ste 130 · Raleigh, NC 27608   "
open_f = SANS(21, True)
wf = put(ft, foot, LX, 548, (CREAM[0] - 40, CREAM[1] - 40, CREAM[2] - 44), "foot-a")
put("Open daily", open_f, LX + wf, 548, SUN, "foot-b")

# ---- right art: sun, dashed arc to the moon, songbird on the horizon ----
def ell(box, fill, tag):
    if box[0] < ART_LEFT: fails.append(f"art {tag}: left {box[0]:.0f} < {ART_LEFT}")
    d.ellipse(box, fill=fill)

sun_cx, sun_cy, sun_r = 942, 150, 56
ell([sun_cx - sun_r, sun_cy - sun_r, sun_cx + sun_r, sun_cy + sun_r], SUN, "sun")
d.ellipse([sun_cx - sun_r - 14, sun_cy - sun_r - 14, sun_cx + sun_r + 14, sun_cy + sun_r + 14],
          outline=(150, 112, 70), width=2)

moon_cx, moon_cy, moon_r = 1142, 112, 30
ell([moon_cx - moon_r, moon_cy - moon_r, moon_cx + moon_r, moon_cy + moon_r], CREAM, "moon")

# dashed day-arc between sun and moon (sampled quadratic bezier, alternating segments)
p0 = (sun_cx + sun_r - 6, sun_cy - 12)
p2 = (moon_cx - moon_r - 2, moon_cy + 8)
p1 = ((p0[0] + p2[0]) / 2, 18)
t, on = 0.04, True
while t < 0.94:
    t2 = min(t + 0.07, 0.94)
    if on:
        def bz(tt):
            x = (1-tt)**2*p0[0] + 2*(1-tt)*tt*p1[0] + tt**2*p2[0]
            y = (1-tt)**2*p0[1] + 2*(1-tt)*tt*p1[1] + tt**2*p2[1]
            return x, y
        a, b = bz(t), bz(t2)
        if min(a[0], b[0]) < ART_LEFT: fails.append(f"arc@{t:.2f} left {min(a[0],b[0]):.0f} < {ART_LEFT}")
        d.line([a, b], fill=(196, 108, 84), width=3)
    t, on = t2, not on

for x, y, r in [(872, 92, 3), (906, 214, 2.4), (1052, 58, 2.2), (1163, 222, 3), (1186, 62, 2.6), (880, 302, 2), (1178, 318, 2.5)]:
    if x - r < ART_LEFT: fails.append(f"star@{x}")
    d.ellipse([x - r, y - r, x + r, y + r], fill=(235, 228, 214))

hz_y = 470
d.line([846, hz_y, W, hz_y], fill=(116, 106, 138), width=4)
d.line([880, hz_y, 1052, hz_y], fill=INK, width=10)
d.polygon([(888, hz_y), (906, hz_y - 22), (924, hz_y)], fill=(96, 118, 78))

# bird silhouette (cream on dusk) sitting the horizon, singing right
bx, by = 958, 444
d.polygon([(930, 452), (868, 418), (912, 468)], fill=CREAM)          # tail
d.ellipse([bx - 46, by - 34, bx + 46, by + 34], fill=CREAM)          # body
d.ellipse([914, 424, 962, 452], fill=CORAL2)                         # wing
d.ellipse([1005 - 22, 412 - 22, 1005 + 22, 412 + 22], fill=CREAM)   # head
d.polygon([(1022, 402), (1062, 392), (1024, 416)], fill=SUN)         # beak
d.ellipse([1009, 405, 1015, 411], fill=INK)                          # eye

for bb, col, wdt in [((1074, 358, 1140, 442), CORAL, 5),
                     ((1094, 342, 1184, 462), (196, 102, 76), 4),
                     ((1116, 326, 1236, 480), (160, 88, 70), 3)]:
    if bb[0] < ART_LEFT: fails.append(f"singing arc left {bb[0]} < {ART_LEFT}")
    d.arc(bb, start=-52, end=52, fill=col, width=wdt)

if fails:
    print("OG GUARD FAILS:\n  " + "\n  ".join(fails), file=sys.stderr)
    sys.exit(1)
img.save(OUT, "PNG")
print("wrote", OUT, img.size, "| text right edge max", TEXT_RIGHT, "| art left min", ART_LEFT)
