#!/usr/bin/env bash
# Re-render 13 sub-4K Manim scenes at -qk (3840x2160), then replace manim/BXX.mp4.
set -eo pipefail
cd "$(dirname "$0")"

SCENES=(
  "B02:B02_GreenListBoost"
  "B03:B03_OneProportionZ"
  "B05:B05_TwentyMillion"
  "B07:B07_GradientNotSwitch"
  "B08:B08_TokenFloor"
  "B11:B11_PositivePredictiveValue"
  "B12:B12_ForensicsVersusScreening"
  "B13:B13_UnevenBurden"
  "B15:B15_WallWithDoors"
  "B16:B16_CheapAttack"
  "B18:B18_PrincipalAgent"
  "B19:B19_SelfRetraction"
  "B20:B20_TheCheckThatCorrectedItself"
)

for entry in "${SCENES[@]}"; do
  bid="${entry%%:*}"
  cls="${entry##*:}"
  echo "[$(date +%H:%M:%S)] rendering $bid ($cls) at -qk..."
  manim -qk --disable_caching scenes.py "$cls" >>render_4k.log 2>&1
  out=$(ls -1t media/videos/scenes/2160p24/${cls}.mp4 2>/dev/null | head -1)
  if [ -n "$out" ] && [ -f "$out" ]; then
    cp "$out" "${bid}.mp4"
    echo "[$(date +%H:%M:%S)]   → placed ${bid}.mp4 from $out"
  else
    echo "[$(date +%H:%M:%S)]   FAIL: no output found for $cls" | tee -a render_4k.log
    exit 1
  fi
done
echo "[$(date +%H:%M:%S)] all 13 scenes done."
