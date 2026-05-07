.PHONY: install test validate clean

install:
	python -m pip install -e ".[dev]"

test:
	python -m pytest -v

validate:
	docs-validator ../../docs ../../docs/_examples

clean:
	rm -rf build dist *.egg-info .pytest_cache __pycache__
