from pydantic import BaseModel, field_validator


class NCloudCredential(BaseModel):
    access_key: str
    secret_key: str
    site: str
    
    @classmethod
    @field_validator('site')
    def validate_field_site(cls, v):
        if v not in ['gov', 'public']:
            raise ValueError(f"Value {v} is not allowed in property 'site'. Only 'gov' or 'public' is supported.")