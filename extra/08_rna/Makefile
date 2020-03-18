.PHONY: test pdf clean

pdf:
	asciidoctor-pdf README.adoc

test:
	pytest -xv test.py

clean:
	rm -rf __pycache__
