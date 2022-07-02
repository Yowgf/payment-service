.DEFAULT_GOAL :=

LOG_LEVEL ?= CRITICAL
LOG_LEVEL_ARG := -log-level=$(LOG_LEVEL)

arg1 ?=
arg2 ?=
arg3 ?=
arg4 ?=

.PHONY: clean stubs

clean:

%pb2_grpc.py: $(wildcard src/*.proto)
	python3 src/protogen.py $(LOG_LEVEL_ARG)

%pb2.py: %pb2_grpc.py
	echo in rule 2

stubs: src/bank_pb2.py src/store_pb2.py

run_serv_banco: stubs
	python3 src/bank_server_main.py $(arg1) $(arg2) $(LOG_LEVEL_ARG)

run_cli_banco: stubs
	python3 src/bank_client_main.py $(arg1) $(arg2) $(LOG_LEVEL_ARG)

run_serv_loja: stubs
	python3 src/store_server_main.py $(arg1) $(arg2) $(arg3) $(arg4) $(LOG_LEVEL_ARG)

run_cli_loja: stubs
	python3 src/store_client_main.py $(arg1) $(arg2) $(arg3) $(LOG_LEVEL_ARG)
