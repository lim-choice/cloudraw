from typing import Union
from argparse import ArgumentParser
from configparser import ConfigParser
from models.base import NcloudCredential


SERVICE = [
    "vpc",
    "subnet",
    "acl",
    "vm",
    "acg",
    "lb",
    "mysql",
    "mssql",
    "postgres",
    "redis",
    "mongo"
]


class NcloudService:
    def __init__(self):
        pass
    

class NcloudClient:
    def __init__(self):
        parser = ArgumentParser()
        for service in SERVICE:
            parser.add_subparsers(service, required=True)
        parser.add_argument('--profile', action='store', type=str, default='DEFAULT', help='Profile')
        parser.add_argument('-v', '--verbose', action='store', type=bool, default=False, help='Enable debug mode')
        parser.add_argument('-V', '--version', action='store', type=bool, default=False, help='Print version and exit')
        self.parsed_arguments = parser.parse_args()
        
    def _load_profile(self):
        cfg = ConfigParser()
        cfg.read("~/.ncloud/configure")
        cfg.sections()
        try:
            cfg[self.parsed_arguments.profile]
        except KeyError:
            print(f"Profile {cfg[self.parsed_arguments.profile]} is not found.")
            exit(127)
        self.parsed_arguments
        
