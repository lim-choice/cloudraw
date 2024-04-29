from pydantic import BaseModel, field_validator


class NcloudCredential(BaseModel):
    access_key: str
    secret_key: str
    site: str
    
    @classmethod
    @field_validator('site')
    def validate_field_site(cls, v: str):
        if v.lower() not in ['gov', 'public']:
            raise ValueError(f"Value {v} is not allowed in property 'site'. Only 'gov' or 'public' is supported.")

