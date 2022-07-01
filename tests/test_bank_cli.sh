#!/bin/bash

set -e

tempresults=test_bank_cli_temp
tempbank=tempbank
tempstore=tempstore
inputfpath=fixtures/inputs_bank_cli_1.txt
outputfpath=fixtures/outputs_bank_cli_1.txt

nohup ./debug_bank_srv.sh 2>&1 > $tempbank &
nohup ./debug_store_srv.sh 2>&1 > $tempstore &

cat $inputfpath | ./debug_bank_cli.sh > $tempresults

actual=$(cat $tempresults)
expected=$(cat $outputfpath)

if [ "$actual" != "$expected" ]; then
    echo Test failed. Displaying diff below.
    diff $tempresults $outputfpath
    exit 1
else
    echo Test succeeded
fi

rm $tempbank
rm $tempstore
rm $tempresults
