#!/bin/bash

set -ex

tempresults=test_bank_cli_temp
tempbank=tempbank
tempstore=tempstore
inputfpath=fixtures/inputs_store_cli_1.txt
outputfpath=fixtures/outputs_store_cli_1.txt

function cleanup_procs {
    echo Cleaning up processes
    processes=$(lsof -i :5555,5556 | tail -n +2 | awk '{print $2}')
    [ -z "$processes" ] && return
    kill -9 $processes
}

nohup ./debug_bank_srv.sh 2>&1 > $tempbank &
nohup ./debug_store_srv.sh 2>&1 > $tempstore &
# Wait for servers to start
sleep 0.2

cat $inputfpath | ./debug_store_cli.sh > $tempresults

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
rm $tempstore
rm $tempresults
