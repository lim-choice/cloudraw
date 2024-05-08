import os
import sys
from typing import Union
from argparse import ArgumentParser, _SubParsersAction
from configparser import ConfigParser
from services.vpc import NcloudVPC
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec
from models.base import NcloudCredential
from models.dtype import NcloudServiceList



class NcloudClient:
    def __init__(self, sysargv: list[str]):
        self.VERSION = "Nclient 1.0"
        self.DEBUG = True
        self.load_profile()
    
    def matching_service(self):
        pass

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

    def __version__(self):
        return self.VERSION