from services import Singleton
from src.models.base import NCloudCredential


class ResourceManager(Singleton):
    def __init__(self, credential: NCloudCredential, **params):
        super().__init__(credential, **params)
        