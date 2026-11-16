#!/usr/bin/env python3
"""sheet_all.py <pct> -> contact sheets (4x5 of 640x360) of every Manim beat at pct% in scratchpad/lecture-1/all_<pct>_<n>.png"""
import subprocess, sys, json
from pathlib import Path
from PIL import Image, ImageDraw
HERE=Path(__file__).resolve().parent
S=Path("/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1")
pct=float(sys.argv[1]); ids=[b['beat_id'] for b in json.load(open(HERE/'beat_sheet.json'))['beats'] if b['lane']=='manim']
for n in range(0,len(ids),20):
    W=Image.new('RGB',(640*4,360*5),'white'); dr=ImageDraw.Draw(W)
    for k,b in enumerate(ids[n:n+20]):
        f=HERE/'clips'/f'{b}.mp4'
        d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
        o=S/f'a_{b}.png'
        subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(d*pct/100),'-i',str(f),'-frames:v','1','-vf','scale=640:360',str(o)],check=True)
        im=Image.open(o); W.paste(im,((k%4)*640,(k//4)*360)); dr.text(((k%4)*640+6,(k//4)*360+4),b,fill=(200,40,40))
    W.save(S/f'all_{int(pct)}_{n//20}.png'); print(S/f'all_{int(pct)}_{n//20}.png')
