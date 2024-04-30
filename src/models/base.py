from pydantic import BaseModel, field_validator
from argparse import ArgumentParser


class NcloudCredential(BaseModel):
    access_key: str
    secret_key: str
    site: str
    
    def __init__(self, access_key: str, secret_key: str, site: str):
        self.access_key = access_key
        self.secret_key = secret_key
        self.site = site
    
    @classmethod
    @field_validator('site')
    def validate_field_site(cls, v: str):
        if v.lower() not in ['gov', 'public']:
            raise ValueError(f"Value {v} is not allowed in property 'site'. Only 'gov' or 'public' is supported.")


class NcloudParser:
    def __init__(self, parser: ArgumentParser):
        self.parser = parser