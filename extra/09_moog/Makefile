.PHONY: test pdf clean

pdf:
	asciidoctor-pdf README.adoc

test:
	pytest -xv --disable-pytest-warnings test.py

clean:
	rm -rf __pycache__ .pytest
