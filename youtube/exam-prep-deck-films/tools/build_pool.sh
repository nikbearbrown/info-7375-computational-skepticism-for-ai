#!/bin/zsh
# build_pool.sh WORKER - take the next unclaimed film (mkdir lock), build it, retry once from resheet if it stopped short.
cd "${0:A:h}/.."
for n in 07 03 02 05 04 08 06 10 09 12 11 13; do
  [ -f extract/$n/READY ] || continue
  mkdir extract/$n/.claim 2>/dev/null || continue
  python3 tools/build_film.py $n --from sheet --to checks > logs/ex-$n.log 2>&1
  echo "$n exit $? (worker $1)" >> logs/pool.log
  if ! grep -q "stages done: .*checks" logs/ex-$n.log; then
    python3 tools/build_film.py $n --from resheet --to checks > logs/ex-$n-retry.log 2>&1
    echo "$n retry exit $? (worker $1)" >> logs/pool.log
  fi
done
echo "worker $1 done" >> logs/pool.log
