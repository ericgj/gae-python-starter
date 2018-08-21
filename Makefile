
ENV ?= production
SERVICE ?= default

deploy: test build
	bin/deploy $(ENV) $(SERVICE)
    bin/deploy-static 

test:
	bin/test $(SERVICE)

build:
	bin/build $(ENV) $(SERVICE)

.PHONY: deploy test build
