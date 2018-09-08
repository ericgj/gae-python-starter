
SERVICE ?= default

deploy-prod: test build-prod
	bin/deploy production $(SERVICE)
	bin/deploy-static

deploy: test build-staging
	bin/deploy staging $(SERVICE)
	bin/deploy-static 

test: build-dev
	bin/test $(SERVICE)

dev-server: build-dev
	bin/dev-server $(SERVICE)

build-prod:
	bin/build production $(SERVICE)

build-staging:
	bin/build staging $(SERVICE)

build-dev:
	bin/build development $(SERVICE)

.PHONY: deploy deploy-prod test dev-server build-prod build-staging build-dev
