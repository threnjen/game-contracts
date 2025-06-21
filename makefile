# ────────────────────────── CONFIG ──────────────────────────
PYTHON := $(shell \
    command -v python3 2>/dev/null || \
    command -v python  2>/dev/null || \
    command -v py      2>/dev/null )

# Convert path to Windows form if we're in Git Bash
ifeq ($(OS),Windows_NT)
    ifneq (,$(findstring /,$(PYTHON)))
        PYTHON := $(shell cygpath -w "$(PYTHON)")
    endif
endif

ifeq ($(PYTHON),)
$(error "No Python interpreter found. Install Python and ensure it's on PATH.")
endif

VENV_DIR    ?= .venv
PKG_NAME    ?= game_contracts          # <── replace with your import-root / package dir
DIST_DIR    ?= dist

# Detect the venv’s Python & Pip once the venv exists
VENV_PY     := $(VENV_DIR)/Scripts/python.exe
VENV_PIP    := $(VENV_DIR)/Scripts/pip.exe
ifeq ($(OS),Linux)
VENV_PY     := $(VENV_DIR)/bin/python
VENV_PIP    := $(VENV_DIR)/bin/pip
endif
ifeq ($(OS),Darwin)
VENV_PY     := $(VENV_DIR)/bin/python
VENV_PIP    := $(VENV_DIR)/bin/pip
endif

# ─────────────────────── STANDARD TARGETS ───────────────────

.PHONY: help
help:                          ## Show all commands
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS=":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: $(VENV_DIR)/SUCCESS       ## Create venv (+ upgrade pip & build)
$(VENV_DIR)/SUCCESS:
	$(PYTHON) -m venv $(VENV_DIR)
	$(PYTHON) -m pip install --upgrade pip build
	@echo "done" > $@

.PHONY: install
install: venv                   ## Install project in editable mode into venv
	$(VENV_PY) -m pip install -e ".[dev]"   # grabs dev-deps if declared

.PHONY: package
package: venv clean_dist        ## Build wheel & sdist under dist/
	$(VENV_PY) -m build --sdist --wheel --outdir $(DIST_DIR)
	@echo "Built packages: $(shell ls -1 $(DIST_DIR))"

.PHONY: clean_dist
clean_dist:                     ## Remove dist/ before re-packaging
	@rm -rf $(DIST_DIR)
	@mkdir -p $(DIST_DIR)

.PHONY: clean
clean:                          ## Remove venv & build artifacts
	@rm -rf $(VENV_DIR) $(DIST_DIR) *.egg-info

# ─────────────────────── ADVANCED TARGETS ───────────────────

.PHONY: shell
shell: venv                     ## Activate venv in a new shell
ifeq ($(OS),Windows_NT)
	@cmd /K "$(VENV_DIR)\Scripts\activate.bat"
else
	@/bin/bash -c "source $(VENV_DIR)/bin/activate && bash"
endif

.PHONY: gh-install
gh-install:                     ## (For CI) pip-install directly from GitHub @ main
	pip install "git+https://github.com/threnjen/$(PKG_NAME).git@main#egg=$(PKG_NAME)"

.PHONY: test
test: venv                      ## Run tests (pytest) inside venv
	$(VENV_PY) -m pytest -q

# default goal
.DEFAULT_GOAL := help
