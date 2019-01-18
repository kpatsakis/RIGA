#!/bin/bash

mkdir -p test_files
cd test_files

for i in `seq 1 50`;
do
  # create a random file
  head -c 4K </dev/urandom >tmpfile
  # find the hash that it will have
  hash=$(ipfs add -n -q tmpfile | head -n 1)
  ipfs add -q tmpfile > /dev/null
  ts=$(date +%s%3N)
  curl -s "https://cloudflare-ipfs.com/ipfs/$hash" --output out
  te=$(date +%s%3N)
  echo "$(($te-$ts))"

done
cd ..
