.PHONY: install format lint test

install:
    pip install -r requirements.txt

format:
    black test/

lint:
    flake8 test/

test:
    pytest test/
