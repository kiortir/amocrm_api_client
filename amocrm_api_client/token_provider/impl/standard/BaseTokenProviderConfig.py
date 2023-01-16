from pydantic import BaseModel


__all__ = [
    "StandardTokenProviderConfig",
]


class BaseTokenProviderConfig(BaseModel):

    integration_id: str
    secret_key: str
    auth_code: str
    base_url: str
    redirect_uri: str
