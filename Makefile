.PHONY: clean

clean:
	find . -type d -name \*cache\* -maxdepth 2 -exec rm -rf {} \;
	find . -name .log -delete
