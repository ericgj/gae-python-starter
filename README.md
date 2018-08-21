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


# Run tests on default service
bin/test

# Run (pre-build) tests on non-default service
bin/test service1


# Test, build, and deploy to production default service, and static files
make deploy

# Test, build, and deploy to staging non-default service, and static files
ENV=staging SERVICE=service1 make deploy


```
