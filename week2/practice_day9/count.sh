#!/bin/bash
echo "Counting sequences in: $1"
grep -c ">" "$1"
