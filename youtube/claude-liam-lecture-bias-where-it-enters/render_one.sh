#!/bin/bash
# usage: render_one.sh <Class> [quality flag e.g. -ql] ; renders the last frame to scratch with its own media_dir
R="$(cd "$(dirname "$0")" && pwd)"
S=/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-6
C=$1; Q=${2:--ql}
mkdir -p $S/stills/$C
cd $R && manim $Q -s --media_dir $S/stills/$C scenes.py $C 2>&1 | tail -3
find $S/stills/$C -name "*.png" | head -1
