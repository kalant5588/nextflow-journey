#!/bin/bash

if [ -z "$1" ]; then
  echo "Please give me a FASTA file. Example: ./count_seqs.sh insulin.fasta"
  exit 1
fi

echo "Counting sequences in: $1"
grep -c ">" "$1"
