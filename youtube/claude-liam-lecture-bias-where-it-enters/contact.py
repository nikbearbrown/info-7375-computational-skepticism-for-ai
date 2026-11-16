#!/usr/bin/env python3
"""contact.py <out.png> <Class> ... : contact sheet of last-frame stills from the scratch folder (3 columns)."""
import sys, glob
from PIL import Image, ImageDraw
S = "/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-6/stills"
out, names = sys.argv[1], sys.argv[2:]
ims = []
for n in names:
    f = glob.glob(f"{S}/{n}/images/scenes/*.png")
    if f:
        im = Image.open(f[0]).convert("RGB").resize((640, 360)); d = ImageDraw.Draw(im); d.rectangle((0, 0, 330, 20), fill=(255, 255, 255)); d.text((4, 4), n, fill=(0, 0, 0)); ims.append(im)
cols = 3; rows = (len(ims) + cols - 1) // cols
sheet = Image.new("RGB", (cols * 644, rows * 364), (200, 200, 200))
for i, im in enumerate(ims): sheet.paste(im, ((i % cols) * 644, (i // cols) * 364))
sheet.save(out); print(out, len(ims))
