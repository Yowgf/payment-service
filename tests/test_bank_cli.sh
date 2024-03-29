#!/bin/bash

set -e

tempresults=test_bank_cli_temp
tempbank=tempbank
tempstore=tempstore
inputfpath=fixtures/inputs_bank_cli_1.txt
outputfpath=fixtures/outputs_bank_cli_1.txt

function cleanup_procs {
    echo Cleaning up processes
    processes=$(lsof -i :5555 | tail -n +2 | awk '{print $2}')
    [ -z "$processes" ] && return
    kill -9 $processes
}

nohup ./debug_bank_srv.sh 2>&1 > $tempbank &
# Wait for server to start
sleep 0.2

cat $inputfpath | ./debug_bank_cli.sh > $tempresults

actual=$(cat $tempresults)
expected=$(cat $outputfpath)

if [ "$actual" != "$expected" ]; then
    echo Test failed. Displaying diff below.
    diff $tempresults $outputfpath || true
    cleanup_procs
    exit 1
else
    echo Test succeeded
fi

cleanup_procs
rm $tempbank
rm $tempresults
