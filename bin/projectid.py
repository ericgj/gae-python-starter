#!/usr/bin/env python

import sys
import os.path
from ruamel import yaml

def read_project_id(project_file):
    data = None
    with open(project_file, 'r') as f:
        data = yaml.safe_load(f)
    if data is None:
        data = {}
    return data.get('id')

def write_project_id(project_file, newval):
    data = None
    if os.path.isfile( project_file ):
        with open(project_file, 'r') as f:
            data = yaml.safe_load(f)
    if data is None:
        data = {}
    data['id'] = newval
    with open(project_file, 'w') as f:
        f.write(yaml.dump(data))


if len(sys.argv) < 1:
    sys.stderr.write("Usage: %s environ [new-project-id]\n" % sys.argv[0])
    exit(1)

env = sys.argv[1]
newval = None
if len(sys.argv) >= 3:
    newval = sys.argv[2]

env_dir = os.path.join("config", env)
project_file = os.path.join( env_dir, "project.yaml" )

# read
if not newval is None:
    write_project_id(project_file, newval)
print( read_project_id(project_file) )


