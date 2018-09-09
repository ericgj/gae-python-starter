
SERVICE ?= default

test: build-dev
	bin/test $(SERVICE)

dev-server: build-dev
	bin/dev-server $(SERVICE)

build-prod:
	bin/build production $(SERVICE)

build-staging:
	bin/build staging $(SERVICE)

build-test:
	bin/build test $(SERVICE)

build-dev:
	bin/build development $(SERVICE)

.PHONY: test dev-server build-prod build-staging build-test build-dev
