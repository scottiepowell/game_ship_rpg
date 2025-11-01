.PHONY: setup test run lint format cli clean help

# Simple venv shortcuts
VENV := venv
PY   := $(VENV)/bin/python
PIP  := $(VENV)/bin/pip

help:
	@echo "Targets:"
	@echo "  setup   - create venv and install requirements"
	@echo "  test    - run pytest"
	@echo "  run     - launch Kivy app"
	@echo "  cli     - run Click CLI"
	@echo "  lint    - flake8 on src/"
	@echo "  format  - black on src/"
	@echo "  clean   - remove venv and caches"

setup:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

test:
	$(PY) -m pytest

run:
	$(PY) -m src.kivy_app.main

cli:
	$(PY) cli.py

lint:
	$(VENV)/bin/flake8 src

format:
	$(VENV)/bin/black src

clean:
	rm -rf $(VENV) __pycache__ .pytest_cache