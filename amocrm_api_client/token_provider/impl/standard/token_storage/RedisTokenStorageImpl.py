from typing import Any, Mapping

import jwt

from .ITokenStorage import ITokenStorage
from .TokenStorageImpl import TokenStorageImpl


class RedisTokenStorageImpl(TokenStorageImpl):
    from redis import asyncio as aioredis

    def __init__(
        self,
        redis_client: aioredis.Redis,
        encryption_key: str = "secret",
        redis_key: str = "amo_tokens",
        **_
    ) -> None:
        self.__client = redis_client
        self.__encryption_key = encryption_key
        self.key = redis_key

    async def _save_data(self, data: dict[str, Any]) -> None:
        encoded_str = jwt.encode(
            payload=data,
            key=self.__encryption_key,
            algorithm="HS256"
        )

        await self.__client.set(self.key, encoded_str)

    async def _recover_data(self) -> dict[str, Any]:
        encoded_str: str | None = await self.__client.get(self.key)

        if encoded_str is None:
            return dict()

        data: dict[str, Any] = jwt.decode(
            jwt=encoded_str,
            key=self.__encryption_key,
            algorithms=["HS256"],
        )
        return data

    async def clear(self) -> None:
        await self.__client.delete(self.key)

    class Config(ITokenStorage.Config):
        from redis import asyncio as aioredis

        redis_client: aioredis.Redis
        encryption_key: str = "secret"
