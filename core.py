import os
import sys
from typing import Union
from argparse import ArgumentParser, _SubParsersAction
from configparser import ConfigParser
from models.base import NcloudCredential
from models.dtype import NcloudServiceList
from services.vpc import NcloudVPC
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec


class NcloudClient:
    def __init__(self):
        self.VERSION = "Nclient 1.0"
        self.DEBUG = True
        self.load_profile()
        project_root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        
        parser = ArgumentParser(prog="Nclient")
        parser.add_argument('-p', '--profile', action='store', type=str, default='DEFAULT', help='Profile')
        parser.add_argument('--debug', action='store_true', default=False, help='Enable debug mode')
        parser.add_argument('-v', '--version', action='version', version=f"{self.VERSION}", help='Print version and exit')
        
        subparser = parser.add_subparsers(title="Supported Service", dest="subcommand")
        for service in NcloudServiceList:
            subparser.add_parser(name=service.value)
        args = parser.parse_args()
        
        print(f"Subcommand = {args.subcommand}")
        dynamic_command_value = NcloudServiceList._value2member_map_[args.subcommand].name
        print(f"dynamic command value = {dynamic_command_value}")
        dynamic_class_value = f"Ncloud{dynamic_command_value}"
        print(f"dynamic class value = {dynamic_class_value}")
        file_path = f"{project_root}/services/{args.subcommand}.py"
        
        
        
        
        
        
        
    def load_profile(self, profile_name = "DEFAULT"):
        cfg = ConfigParser()
        cfg.read(self.__load_config())
        try:
            cfg[profile_name]
        except KeyError:
            print(f"Profile {cfg[profile_name]} is not found.")
            exit(127)

    def __load_config(self):
        return os.path.join(os.path.expanduser('~'), '.ncloud', 'configure')
