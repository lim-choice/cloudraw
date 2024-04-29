from typing import Union
from models.base import NcloudCredential
from enum import Enum

class SUBPARSER:
    pass


class NcloudService:
    def __init__(self):
        pass
    

class NcloudClient:
    def __init__(self, credential: NcloudCredential):
        self.credential = credential