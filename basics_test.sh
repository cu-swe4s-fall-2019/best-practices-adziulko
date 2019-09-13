#!/bin/#!/usr/bin/env bash

chmod +x run.sh

conda activate swe4s

test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

(for i in 'seq 1 100'; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run basic_test python get_column_stats.py --file_name data.txt --column_number 2
assert_in_stdout 2
assert_exit_code 0

echo 'running pycodestyle on style.py'
pycodestyle style.py

echo 'running pycodestyle on get_column_stats.py'
pycodestyle get_column_stats.py

(for i in 'seq 1 100'; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py --file_name data.txt --col_nummber 2


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --file_name data.txt --col_number 2
