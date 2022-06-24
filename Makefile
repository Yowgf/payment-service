
.DEFAULT_GOAL :=

LOG_LEVEL ?= CRITICAL
LOG_LEVEL_ARG := -log-level=$(LOG_LEVEL)

clean:

stubs:

run_serv_banco:

run_cli_banco:
	python3 src/bank_client_main.py $(arg1) $(arg2) $(LOG_LEVEL_ARG)

run_serv_loja:

run_cli_loja:

