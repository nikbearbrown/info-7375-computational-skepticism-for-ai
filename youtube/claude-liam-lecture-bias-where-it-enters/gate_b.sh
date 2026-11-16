#!/bin/bash
# Gate B pre-audit over every Manim class: prints only the classes that are not CLEAN.
R="$(cd "$(dirname "$0")" && pwd)"; cd $R
for c in $(grep -o '^class B[0-9]*_[A-Za-z0-9]*' scenes.py | awk '{print $2}'); do
  out=$(python3 /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class $c --curve-strict 2>&1 | tr '\r' '\n' | grep -E "^\[audit\] scenes|WARN|FAIL|BLOCK|MAJOR|overlap" )
  echo "$out" | grep -q "CLEAN" || { echo "== $c"; echo "$out" | head -6; }
done
echo GATE-B-DONE
