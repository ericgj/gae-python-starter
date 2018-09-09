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


# Build and run tests on default service
make test

# Build and run tests on non-default service
SERVICE=service1 make test


# Initialize SSL files for dev server (run once)
bin/init-dev-server

# Build default service using development config and run dev server
make dev-server


# Initialize bucket for static files deploy (run once)
bin/init-static my-gae-project-id

# Initialize bucket for config files deploy (run once)
bin/init-static-config my-gae-project-id


```


## File structure

```

.env-default
.env-dev
bin/
requirements.txt                # non-frozen build dependencies
config/
    backend-templates
        single/
            app.yaml
        multi/
            common/
            default/
                app.yaml
                dispatch.yaml
    production/
    development/
backend/
    requirements-.txt           # non-frozen dependencies
    requirements.txt            # frozen dependencies
    common/                     # common source code for all services
        model/
    default/                    # note the naming convention under services are up to you
        app.yaml                    # template for app.yaml
        dispatch.yaml               # template for dispatch.yaml
        main.py
    service1/
        app.yaml                # template for service1 app.yaml
        main.py

build/                          # a service at a time
    requirements-.txt
    requirements.txt
    app.yaml
    dispatch.yaml
    main.py
    common/
        model/


```

