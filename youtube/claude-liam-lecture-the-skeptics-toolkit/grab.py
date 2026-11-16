#!/usr/bin/env python3
"""grab.py B13@50 B28@50 ... -> contact sheet at scratchpad/lecture-1/grab.png (frames from clips/)"""
import subprocess, sys
from pathlib import Path
from PIL import Image
HERE=Path(__file__).resolve().parent
S=Path("/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1")
ims=[]
for a in sys.argv[1:]:
    b,_,p=a.partition('@'); p=float(p or 50)
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(HERE/'clips'/f'{b}.mp4')]))
    out=S/f'g_{b}_{int(p)}.png'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(d*p/100),'-i',str(HERE/'clips'/f'{b}.mp4'),'-frames:v','1','-vf','scale=960:540',str(out)],check=True)
    ims.append(Image.open(out))
cols=2; rows=(len(ims)+1)//2
W=Image.new('RGB',(960*cols,540*rows),'white')
for i,im in enumerate(ims): W.paste(im,((i%cols)*960,(i//cols)*540))
W.save(S/'grab.png'); print(S/'grab.png')
