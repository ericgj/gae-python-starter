#!/usr/bin/env python

import os.path
from functools import reduce
from urllib.parse import urlparse
from argparse import ArgumentParser
from ruamel import yaml

def load_yaml(fname):
    data = {}
    with open(fname) as f:
        data = yaml.safe_load(f)
    return data
    
def gunicorn_env_args( vars ):
    def _accum(acc, pair):
        acc.append("--env")
        acc.append("%s='%s'" % pair)
        return acc
    return reduce( _accum, vars.items(), [] )


# parse args

argparser = ArgumentParser(description="Generate script for dev-server")
argparser.add_argument("app_config", 
                       help="app.yaml file")
argparser.add_argument("src_dir",
                       help="path to app source files")
argparser.add_argument("app_module",
                       help="MODULE:VARIABLE reference to WSGI app")
argparser.add_argument("--project-id", default=None,
                       help="GAE Project ID")
argparser.add_argument("--virtualenv", default=".env", 
                       help="path to virtualenv to run server subprocesses under")
argparser.add_argument("--port", default=8080, type=int,
                       help="server port" )
argparser.add_argument("--static-port", default=8081, type=int,
                       help="static server port" )
argparser.add_argument("--static-dir", default="static", 
                       help="static root dir" )
argparser.add_argument("--keyfile", default=None)
argparser.add_argument("--certfile", default=None)
argparser.add_argument("--ca-certs", default=None)


args = argparser.parse_args()


# load yaml

config = load_yaml(args.app_config)
env_vars = config["env_variables"]
if not args.project_id is None:
    env_vars['GOOGLE_CLOUD_PROJECT'] = args.project_id
static_port = args.static_port or urlparse(env_vars['STATIC_BASE_URL']).port

ssl_opts = (
    "" if args.keyfile is None else "--keyfile='%s'" % args.keyfile,
    "" if args.certfile is None else "--certfile='%s'" % args.certfile,
    "" if args.ca_certs is None else "--ca-certs='%s'" % args.ca_certs
)

server_line = """
( . {virtualenv}/bin/activate && cd {src_dir} && gunicorn -b :{server_port} --log-level debug --reload {env_vars} {ssl_opts} {app_module} ) &
""".format( 
    virtualenv=args.virtualenv, 
    src_dir=args.src_dir,
    server_port=str(args.port),
    env_vars=" ".join(gunicorn_env_args(env_vars)),
    ssl_opts=" ".join(ssl_opts),
    app_module=args.app_module
)

static_line = """
( . {virtualenv}/bin/activate && cd {static_dir} && python -m http.server {static_port} ) &
""".format(
    virtualenv=args.virtualenv, 
    static_dir=args.static_dir,
    static_port=str(static_port)
)

print("#!/usr/bin/env bash")
print(server_line)
print(static_line)
print("echo **** To stop development server, CTRL+C ****")
print("wait -n")
print("pkill -P $$")


