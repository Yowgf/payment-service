# Simple Payment Service

Simple payment service implemented as a POC of Python-based gRPC.

The payment service is composed of two separate gRPC services: `Store` and
`Bank`. See `src/bank` for the implementation of the `Bank` service. See
`src/store` for the implementation of the `Store` service.

## Running

This project runs over the Python interpreter, so there is no compilation steps
necessary. See `Makefile` for execution rules that have the prefix `run_`.

## Testing

Check out the folder `tests`. This folder contains scripts that start with
`test_`. These scripts run a simple suite of tests given by the professor which
gave the original specification. The `debug_` scripts can be used to easily
start the Bank and Store servers and clients (CLI).
