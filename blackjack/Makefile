.PHONY: pdf test

pdf:
	pandoc README.md -o README.pdf --pdf-engine=xelatex

test:
	pytest -v test.py
