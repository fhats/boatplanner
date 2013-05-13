.PHONY: clean

clean:
	find . -name '*.pyc' -delete

tests: test
test:
	testify tests
