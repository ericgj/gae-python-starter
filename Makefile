
SERVICE ?= default

deploy: deploy-test

deploy-test: test build-test
	bin/deploy test 
	bin/deploy-static 

deploy-staging: staging build-staging
	bin/deploy staging 
	bin/deploy-static 


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

.PHONY: deploy deploy-test deploy-staging test dev-server build-prod build-staging build-test build-dev
