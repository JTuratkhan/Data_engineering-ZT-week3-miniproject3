.PHONY: install test report

install:
	pip install -r requirements.txt

test:
	pytest tests/

report:
	python src/main.py
