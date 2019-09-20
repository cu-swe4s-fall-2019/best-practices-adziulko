#!/bin/bash

chmod +x basics_test.sh

source ssshtest

(for i in 'seq 1 100'; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt


run basic_test python get_column_stats.py --file_name data.txt --column_number 2
assert_in_stdout
assert_exit_code 0

echo 'running pycodestyle on style.py'
pycodestyle style.py

echo 'running pycodestyle on get_column_stats.py'
pycodestyle get_column_stats.py


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run basic_test python get_column_stats.py --file_name data.txt --column_number 2
assert_in_stdout 1
assert_exit_code 0
