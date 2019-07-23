.PHONY: clean

clean:
	find . -type d -name \*cache\* -maxdepth 2 -exec rm -rf {} \;
	find . -name .log -delete

book:
	./bin/compile.py

toc:
	perl -ne '/^[#]{1,3}\s+(?!-)/ && print' book.md > toc.txt
