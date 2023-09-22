.PHONY: install format lint test

install:
    pip install -r requirements.txt

format:
    black src/ test/

lint:
    flake8 src/ test/

test:
	pytest test
