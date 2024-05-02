import os
from typing import Union
from argparse import ArgumentParser, _SubParsersAction
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
    "mongo",
    "help"
]


class NcloudService:
    def __init__(self):
        pass
    
    def add_arguments(self):
        pass
    

class NcloudClient:
    def __init__(self):
        parser = self._load_arguments()
        
    def _load_arguments(self):
        parser = ArgumentParser()
        parser.add_argument('-p', '--profile', action='store', type=str, default='DEFAULT', help='Profile')
        parser.add_argument('-v', '--verbose', type=bool, default=False, help='Enable debug mode')
        parser.add_argument('-V', '--version', type=bool, default=False, help='Print version and exit')
        subparser = parser.add_subparsers(required=True)
        subparser = self._parsing_subcommand(subparser=subparser)
        parser.parse_args()
        
    def _load_profile(self, profile_name = "DEFAULT"):
        cfg = ConfigParser()
        cfg.read(self._load_config())
        try:
            cfg[profile_name]
        except KeyError:
            print(f"Profile {cfg[profile_name]} is not found.")
            exit(127)

    def _load_config(self):
        return os.path.join(os.path.expanduser('~'), '.ncloud', 'configure')

    def _parsing_subcommand(self, subparser: _SubParsersAction):
        for service in SERVICE:
            _p = subparser.add_parser(service)
            
        return subparser