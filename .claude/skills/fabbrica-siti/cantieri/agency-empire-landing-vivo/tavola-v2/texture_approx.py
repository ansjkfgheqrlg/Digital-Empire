# -*- coding: utf-8 -*-
"""Approssimazioni delle due texture di Max (i file originali non sono sul disco: li mette lui in public/texture/).
Servono SOLO alla tavola per mostrare la composizione; in pagina vanno i suoi file."""
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
import pathlib
HERE = pathlib.Path(__file__).parent

# --- Texture 1: onde di linee puntinate arancioni su nero (1600x900) ---
W, H = 1600, 900
img = Image.new("RGB", (W, H), (4, 3, 2))
d = ImageDraw.Draw(img)
rng = np.random.default_rng(7)
xs = np.arange(0, W, 3)
for k, y0 in enumerate(np.arange(-40, H + 40, 9)):
    ph = rng.uniform(0, 6.28); amp = 26 + 18 * np.sin(k * 0.21)
    ys = y0 + amp * np.sin(xs / 210 + ph) + 14 * np.sin(xs / 61 + ph * 1.7) + 9 * np.sin(xs / 23 + k)
    bright = 0.35 + 0.65 * (0.5 + 0.5 * np.sin(xs / 330 + k * 0.4 + ph))
    for x, y, b in zip(xs, ys, bright):
        if 0 <= y < H:
            c = (int(255 * b), int(105 * b), int(18 * b))
            d.point((int(x), int(y)), fill=c)
img = img.filter(ImageFilter.GaussianBlur(0.35))
glow = img.filter(ImageFilter.GaussianBlur(6))
img = Image.blend(img, glow, 0.35)
img.save(HERE / "tex1-onde.jpg", quality=92)

# --- Texture 2: grana arancione su nero con strisce scure diagonali (1200x800) ---
W, H = 1200, 800
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
def blob(cx, cy, sx, sy): return np.exp(-(((xx - cx) / sx) ** 2 + ((yy - cy) / sy) ** 2))
field = 0.9 * blob(780, 250, 380, 260) + 0.7 * blob(260, 420, 300, 240) + 0.5 * blob(700, 650, 260, 160)
diag = (xx - 0.75 * yy)
streak = 1 - 0.55 * np.exp(-((diag - 380) / 40) ** 2) - 0.35 * np.exp(-((diag - 470) / 22) ** 2) - 0.25 * np.exp(-((diag - 300) / 60) ** 2)
noise = rng.random((H, W)).astype(np.float32)
grain = (noise ** 2.2) * 1.4
lum = np.clip(field * streak * grain, 0, 1)
r = (lum * 255).astype(np.uint8); g = (lum * 92).astype(np.uint8); b = (lum * 10).astype(np.uint8)
img2 = Image.fromarray(np.dstack([r, g, b]))
img2 = Image.blend(img2, img2.filter(ImageFilter.GaussianBlur(1.2)), 0.25)
img2.save(HERE / "tex2-grana.jpg", quality=92)
print("ok")
