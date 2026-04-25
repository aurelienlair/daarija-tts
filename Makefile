.DEFAULT_GOAL := help
SHELL := /bin/bash
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help:
	@echo "❓ help section"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## 🛠️  Create venv and install dependencies
	@echo "🌐 creating virtual environment"
	python3 -m venv $(VENV)
	$(PIP) install -e ".[dev]"

REF_AUDIO ?= reference.wav
REF_TEXT  ?=
SPEED     ?= 0.9

run: ## ▶️  Synthesize and play (FILE=input.txt REF_AUDIO=ref.wav REF_TEXT="..." [SPEED=0.9])
	@echo "🔊 synthesizing audio"
	$(if $(FILE), \
		$(PYTHON) tts.py -f $(FILE) --ref-audio="$(REF_AUDIO)" --ref-text="$(REF_TEXT)" --speed=$(SPEED) --play, \
		$(PYTHON) tts.py "$(TEXT)" --ref-audio="$(REF_AUDIO)" --ref-text="$(REF_TEXT)" --speed=$(SPEED) --play)

test: ## ✅🧪 Run tests
	@echo "✅🧪 running tests"
	$(PYTHON) -m pytest tests -v

lint: ## 🔍 Lint with ruff
	@echo "🔍 linting"
	$(PYTHON) -m ruff check tts.py normalize.py tests

format: ## ✨ Format with ruff
	@echo "✨ formatting"
	$(PYTHON) -m ruff format tts.py normalize.py tests

.PHONY: help install run test lint format
