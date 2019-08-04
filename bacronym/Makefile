.PHONY: test clean cover

clean:
	rm -rf __pycache__ coverage

cover:
	pytest --cov=bacronym --cov-report html:coverage test_bacronym.py

test:
	pytest -xv test.py bacronym.py
