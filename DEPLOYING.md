# Google App Engine | Python | Starter

Deployment rig and project template for Google App Engine 3.x apps
(standard and flex environments).


** Work in progress **

## Basic usage

```sh

# Clone the repo into a new project directory
# You can also download and unzip if you don't want git history
#
git clone git@github.com:ericgj/gae-python-starter.git my-new-project
cd my-new-project
git checkout -b master

# Initialize backend with project ID and either
#  "single" for single service (the default)
#  "multi" for multiple services
#
bin/init my-gae-project-id single


# Add some python requirements
echo "WebOb" >> backend/default/requirements-.txt
echo "WebTest" >> backend/default/requirements-.txt


# Install and freeze requirements
bin/install-app 

# Install and freeze requirements for a non-default service
bin/install-app service1


# Build default service using production config
bin/build

# Build non-default service using alternate config
bin/build staging service1


# Run tests on build, default service
bin/test

# Run tests on build, non-default service
bin/test service1


# Build and run tests on default service
make test

# Build and run tests on non-default service
SERVICE=service1 make test


# Test, build, and deploy to production default service, and static files
make deploy

# Test, build, and deploy to staging non-default service, and static files
ENV=staging SERVICE=service1 make deploy


```


## File structure

```

.env-default
.env-dev
bin/
    init
    install
    freeze
    test
    build
    deploy
    dev-server
requirements.txt
config/
    backend-templates
        single/
            app.yaml
            requirements-.txt
        multi/
            common/
            default/
                app.yaml
                dispatch.yaml
                requirements-.txt
    production/
    development/
backend/
    common/                     # common source code for all services
        model/
    default/                    # note the naming convention under services are up to you
        app.yaml                    # template for app.yaml
        dispatch.yaml               # template for dispatch.yaml
        v2.default.app.yaml         # template for v2 of app
        main.py
        v2.py
    service1/
        service1.app.yaml           # template for service1 app.yaml
        main.py

build/                          # a service at a time
    app.yaml
    v2.default.app.yaml
    dispatch.yaml
    main.py
    v2.py
    common/
        model/


```

