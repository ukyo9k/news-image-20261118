#!/usr/bin/env python3
"""Render the front-page poster for Wednesday 18 November 2026 world news.

Draws entry.png (1024x1024) with PIL + DejaVu fonts only. Every story was
verified against sources opened on 18-19 Nov 2026 (Reuters, AP, NASA,
Smithsonian, Just Security). Run: python3 build_poster.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 33, 61)
RED = (185, 28, 28)
GOLD = (176, 141, 44)
GREY = (90, 92, 96)
LIGHT = (255, 255, 255)
SEA = (207, 227, 238)
SAND = (232, 220, 192)
RULE = (20, 33, 61)

F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
F_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading, max_lines=None):
    lines = wrap(draw, text, fnt, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


def star(draw, cx, cy, r, color):
    """Eight-point burst marker."""
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=color)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 92], fill=INK)
    d.rectangle([0, 92, W, 98], fill=RED)
    d.text((24, 14), "THE WORLD TODAY", font=font(F_SERIF_B, 46), fill=LIGHT)
    d.text((24, 66), "22 STORIES  ·  6 CONTINENTS  ·  ALL VERIFIED",
           font=font(F_SANS_B, 14), fill=(200, 205, 215))
    d.text((W - 24, 12), "WEDNESDAY", font=font(F_SANS_B, 26), fill=GOLD, anchor="ra")
    d.text((W - 24, 44), "18 NOVEMBER 2026", font=font(F_SANS_B, 22), fill=LIGHT, anchor="ra")
    d.text((W - 24, 72), "FRONT PAGE — ONE DAY IN ONE IMAGE",
           font=font(F_SANS, 12), fill=(200, 205, 215), anchor="ra")

    # ---------- hero ----------
    hx, hy, hw, hh = 24, 112, 612, 224
    d.text((hx, hy), "THE GULF  —  WAR", font=font(F_SANS_B, 20), fill=RED)
    d.text((hx, hy + 28), "GULF WAR", font=font(F_SERIF_B, 56), fill=INK)
    d.text((hx, hy + 90), "FLARES AGAIN", font=font(F_SERIF_B, 56), fill=INK)
    y = para(d, hx, hy + 158,
         "Iran strikes Kuwait and Bahrain at dawn; US jets bomb a missile "
         "site on Qeshm Island; Houthis hit Saudi pipeline pumps.",
         font(F_SANS, 19), INK, hw, 24, max_lines=3)
    d.text((hx, y + 4), "Third Iranian attack on US targets in Bahrain in five days — after a two-month lull.",
           font=font(F_SANS, 14), fill=GREY)

    # hero schematic map panel
    mx, my, mw, mh = 660, 112, 340, 224
    d.rectangle([mx, my, mx + mw, my + mh], fill=SEA, outline=INK, width=2)
    # land: Iran (top) and Arabia (bottom)
    d.polygon([(mx, my), (mx + mw, my), (mx + mw, my + 52),
               (mx + 210, my + 44), (mx + 120, my + 58), (mx, my + 48)],
              fill=SAND)
    d.polygon([(mx, my + mh), (mx + mw, my + mh), (mx + mw, my + 168),
               (mx + 250, my + 158), (mx + 90, my + 176), (mx, my + 162)],
              fill=SAND)
    d.text((mx + 12, my + 8), "IRAN", font=font(F_SANS_B, 15), fill=INK)
    d.text((mx + 12, my + mh - 26), "SAUDI ARABIA", font=font(F_SANS_B, 13), fill=INK)
    d.text((mx + 150, my + 96), "THE GULF", font=font(F_SANS_B, 14), fill=(40, 90, 130))
    # Qeshm island + markers
    d.ellipse([mx + 240, my + 100, mx + 276, my + 118], fill=SAND, outline=INK)
    star(d, mx + 258, my + 109, 12, RED)
    d.text((mx + 258, my + 122), "QESHM", font=font(F_SANS_B, 11), fill=INK, anchor="ma")
    d.text((mx + mw - 10, my + 150), "STRAIT OF HORMUZ →",
           font=font(F_SANS_B, 12), fill=(40, 90, 130), anchor="ra")
    star(d, mx + 84, my + 78, 11, RED)
    d.text((mx + 100, my + 70), "KUWAIT", font=font(F_SANS_B, 12), fill=INK)
    star(d, mx + 52, my + 118, 11, RED)
    d.text((mx + 66, my + 110), "BAHRAIN", font=font(F_SANS_B, 12), fill=INK)
    d.text((mx + 10, my + mh - 52), "SCHEMATIC MAP — NOT TO SCALE",
           font=font(F_SANS, 10), fill=GREY)

    d.line([24, 352, W - 24, 352], fill=RULE, width=2)

    # ---------- top 3 ----------
    top3 = [
        ("APEC — SHENZHEN", "TRUMP HUGS XI AS TRILATERAL OPENS",
         "Xi vows to fight protectionism as Putin joins the talks in "
         "Shenzhen.", "globe"),
        ("CHIPS — EARNINGS", "NVIDIA'S $115.8BN RECORD QUARTER",
         "Revenue up 103% in its first results since Huang quit; the board "
         "rules out his return.", "chip"),
        ("USA — SENATE", "DEMOCRATS TAKE 56–44 MAJORITY",
         "Peltola wins Alaska — the ninth flip, the largest Senate majority "
         "since 2009.", "vote"),
    ]
    col_w = 320
    for i, (kick, head, deck, icon) in enumerate(top3):
        x = 24 + i * (col_w + 8)
        y = 366
        # icon tile
        d.rectangle([x, y, x + 44, y + 44], fill=INK)
        if icon == "globe":
            d.ellipse([x + 8, y + 8, x + 36, y + 36], outline=GOLD, width=2)
            d.line([x + 8, y + 22, x + 36, y + 22], fill=GOLD, width=2)
            d.arc([x + 15, y + 8, x + 29, y + 36], 270, 90, fill=GOLD, width=2)
            d.arc([x + 15, y + 8, x + 29, y + 36], 90, 270, fill=GOLD, width=2)
        elif icon == "chip":
            d.rectangle([x + 12, y + 12, x + 32, y + 32], outline=GOLD, width=2)
            for px in (16, 22, 28):
                d.line([x + px, y + 6, x + px, y + 12], fill=GOLD, width=2)
                d.line([x + px, y + 32, x + px, y + 38], fill=GOLD, width=2)
                d.line([x + 6, y + px, x + 12, y + px], fill=GOLD, width=2)
                d.line([x + 32, y + px, x + 38, y + px], fill=GOLD, width=2)
        else:  # vote
            d.rectangle([x + 9, y + 18, x + 35, y + 36], outline=GOLD, width=2)
            d.line([x + 14, y + 28, x + 20, y + 33], fill=GOLD, width=3)
            d.line([x + 20, y + 33, x + 31, y + 16], fill=GOLD, width=3)
        d.text((x + 54, y + 2), kick, font=font(F_SANS_B, 13), fill=RED)
        y = para(d, x, y + 50, head, font(F_SANS_B, 20), INK, col_w, 23,
                 max_lines=2)
        para(d, x, y + 4, deck, font(F_SANS, 14), (40, 40, 40), col_w, 17,
             max_lines=2)

    d.line([24, 500, W - 24, 500], fill=RULE, width=2)

    # ---------- grid 2x3 ----------
    grid = [
        ("UKRAINE — ENERGY WAR",
         "Drones halve Russia's oil refining",
         "Processing down 45% since late Oct.; 15 of 35 big refineries hit "
         "as Kyiv's strikes grow."),
        ("SPACE — VOYAGER 1",
         "One light-day from Earth",
         "First human-made object 16.1bn miles out; a radio signal now "
         "takes a full day to arrive."),
        ("ASIA — DEALS",
         "Indonesia–China sign $71.8bn",
         "Four partnerships incl. 10 smart cities; Prabowo watches on at "
         "the APEC summit."),
        ("MARKETS — GOLD & RATES",
         "Gold slides below $3,800",
         "Down 2%+ to about $3,770 as strong US data turns the Fed "
         "hawkish; October minutes out."),
        ("ISRAEL — IRAN FILE",
         "Mossad chief pushed US for joint Iran strikes",
         "Gofman met the CIA chief in Washington; Netanyahu stays on as "
         "caretaker PM."),
        ("FRANCE — 2027 RACE",
         "Mélenchon 'could beat Le Pen'",
         "Justice minister warns centrists to unite before the runoff; "
         "Le Pen unveils pension plans."),
    ]
    gw, gh = 320, 108
    for i, (kick, head, deck) in enumerate(grid):
        col, row = i % 3, i // 3
        x = 24 + col * (gw + 8)
        y = 514 + row * (gh + 6)
        d.text((x, y), kick, font=font(F_SANS_B, 12), fill=RED)
        y = para(d, x, y + 18, head, font(F_SANS_B, 18), INK, gw, 21,
                 max_lines=2)
        para(d, x, y + 2, deck, font(F_SANS, 13), (40, 40, 40), gw, 16,
             max_lines=2)

    d.line([24, 748, W - 24, 748], fill=RULE, width=2)

    # ---------- also list ----------
    d.text((24, 760), "ALSO ON WEDNESDAY 18 NOVEMBER",
           font=font(F_SANS_B, 17), fill=INK)
    d.line([24, 784, W - 24, 784], fill=RED, width=2)
    also = [
        ("GAZA", "Board of Peace: Israel, Hamas both failing pledges."),
        ("UKRAINE TALKS", "Putin “not ready” for serious peace talks."),
        ("TURKEY", "Prosecutor seeks probe of ex-banking chief Kavcioglu."),
        ("UGANDA", "Mugumya charged with treachery, missing 15 months."),
        ("MYANMAR", "Junta chief says government will review ASEAN ties."),
        ("HORN OF AFRICA", "Ethiopia, Eritrea mass troops on the border."),
        ("AVIATION", "FAA pauses router installs tied to nationwide stop."),
        ("WEATHER", "Cyclone Akvan hits Andhra Pradesh: 110 km/h winds."),
        ("TECH", "Anthropic prices mega-IPO; $60bn+ listing due Thursday."),
        ("INDIA", "Record $10.07bn inflows; Amazon pledges $7bn green."),
        ("CHIPS", "US blocks China's remote access to AI chips."),
        ("AI SAFETY", "Four top AI platforms drafted terror plans if asked."),
    ]
    col_w2 = 480
    for i, (kick, text) in enumerate(also):
        col, row = i % 2, i // 2
        x = 24 + col * (col_w2 + 16)
        y = 796 + row * 30
        d.text((x, y), kick + " — ", font=font(F_SANS_B, 14), fill=RED)
        kw = d.textlength(kick + " — ", font=font(F_SANS_B, 14))
        para(d, x + kw, y, text, font(F_SANS, 14), (30, 30, 30),
             col_w2 - kw, 17, max_lines=1)
        if kw + d.textlength(text, font=font(F_SANS, 14)) > col_w2:
            print("OVERLONG also item:", kick, "excess",
                  round(kw + d.textlength(text, font=font(F_SANS, 14)) - col_w2), "px")

    # ---------- footer ----------
    d.line([24, 978, W - 24, 978], fill=RULE, width=2)
    d.text((24, 986), "Sources: Reuters · AP · NASA · Smithsonian · Just Security — "
           "every story verified 18 Nov 2026. Drawn programmatically.",
           font=font(F_SANS, 12), fill=GREY)
    d.text((W - 24, 986), "make.fun", font=font(F_SANS_B, 12), fill=GREY, anchor="ra")

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
