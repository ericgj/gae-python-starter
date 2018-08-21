
ENV ?= production
SERVICE ?= default

deploy: test
	bin/deploy $(ENV) $(SERVICE)
	bin/deploy-static 

test: build
	bin/test $(SERVICE)

build:
	bin/build $(ENV) $(SERVICE)

.PHONY: deploy test build
