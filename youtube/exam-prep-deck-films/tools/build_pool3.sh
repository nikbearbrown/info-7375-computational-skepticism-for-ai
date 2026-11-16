#!/bin/zsh
cd "${0:A:h}/.."
for n in 13 01 02 03 04 05 06 07 08 09 10 11 12; do
  mkdir extract/$n/.claim3 2>/dev/null || continue
  python3 tools/build_film.py $n --from card --to checks > logs/r3-$n.log 2>&1
  echo "$n exit $? (worker $1)" >> logs/pool3.log
done
echo "worker $1 done" >> logs/pool3.log
