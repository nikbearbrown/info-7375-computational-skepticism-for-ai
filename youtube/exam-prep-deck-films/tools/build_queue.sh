#!/bin/zsh
# build_queue.sh LANE FILM... - build each film once its script is checked (extract/NN/READY exists), in order.
# Two lanes run side by side; each film goes through sheet -> checks (voice, pad, whisper, bookends, capture, review, final, checks).
cd "${0:A:h}/.."
lane=$1; shift
for n in "$@"; do
  while [ ! -f extract/$n/READY ]; do sleep 30; done
  python3 tools/build_film.py $n --from sheet --to checks > logs/ex-$n.log 2>&1
  echo "$n exit $?" >> logs/queue-$lane.log
  # the review cut can stamp the sheet; re-run from resheet once if Gate V or a stale clip stopped it
  if ! grep -q "stages done: .*checks" logs/ex-$n.log; then
    python3 tools/build_film.py $n --from resheet --to checks > logs/ex-$n-retry.log 2>&1
    echo "$n retry exit $?" >> logs/queue-$lane.log
  fi
done
echo "lane $lane done" >> logs/queue-$lane.log
