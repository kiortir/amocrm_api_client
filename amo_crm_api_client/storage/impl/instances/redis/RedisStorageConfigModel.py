from typing import Optional
from pydantic import (
    IPvAnyAddress,
    BaseModel,
    Field,
)


__all__ = [
    "RedisStorageConfigModel",
]


class RedisStorageConfigModel(BaseModel):

    host: str = "127.0.0.1"
    port: int = Field(6379, gt=0, lt=65536)
    database: int = 1
    password: Optional[str] = None
    prefix: str = "amocrm-api-client"