.PHONY: install test report

install:
	pip install -r requirements.txt

test:
	pytest test/

report:
	python src/main.py
