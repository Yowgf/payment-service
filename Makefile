.DEFAULT_GOAL :=

LOG_LEVEL ?= CRITICAL
LOG_LEVEL_ARG := -log-level=$(LOG_LEVEL)

arg1 ?=
arg2 ?=
arg3 ?=
arg4 ?=

clean:

stubs:
	python3 src/protogen.py $(LOG_LEVEL_ARG)

run_serv_banco: stubs
	python3 src/bank_server_main.py $(arg1) $(arg2) $(LOG_LEVEL_ARG)

run_cli_banco: stubs
	python3 src/bank_client_main.py $(arg1) $(arg2) $(LOG_LEVEL_ARG)

run_serv_loja: stubs
	python3 src/store_server_main.py $(arg1) $(arg2) $(arg3) $(arg4) $(LOG_LEVEL_ARG)

run_cli_loja: stubs
	python3 src/store_client_main.py $(arg1) $(arg2) $(arg3) $(LOG_LEVEL_ARG)
