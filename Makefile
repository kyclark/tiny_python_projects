install:
	python3 -m pip install -r requirements.txt

clean:
	find . -name .pytest_cache -o -name __pycache__ -o -name .idea -o -name .mypy_cache -exec rm -rf {} \;

