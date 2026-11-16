#!/bin/zsh
# finish_all.sh - after the pool, retry any film whose newest log does not end with all stages done (up to twice), then summarise.
cd "${0:A:h}/.."
while [ "$(grep -c 'worker .* done' logs/pool.log 2>/dev/null)" -lt 3 ] || pgrep -f "build_film.py" >/dev/null; do sleep 60; done
for pass in 1 2; do
  for n in 01 02 03 04 05 06 07 08 09 10 11 12 13; do
    f=$(ls -t logs/ex-$n*.log logs/neu-01b.log logs/fin-$n-*.log 2>/dev/null | grep -E "ex-$n|fin-$n|neu-01b" | head -1)
    if [ -z "$f" ] || ! tail -3 "$f" | grep -q "stages done: .*checks"; then
      python3 tools/build_film.py $n --from resheet --to checks > logs/fin-$n-$pass.log 2>&1
      echo "$n finish pass $pass exit $?" >> logs/pool.log
    fi
  done
done
for n in 01 02 03 04 05 06 07 08 09 10 11 12 13; do
  f=$(ls -t logs/ex-$n*.log logs/fin-$n-*.log logs/neu-01b.log 2>/dev/null | grep -E "ex-$n|fin-$n|neu-01b" | head -1)
  echo "== $n ($f) $(grep -E '^- master|bookend structure|loudness_check|FAILED' $f | tail -3 | cut -c1-200 | tr '\n' ' ')"
done
