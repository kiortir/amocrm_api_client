from ..BaseTokenProviderConfig import BaseTokenProviderConfig

__all__ = [
    "ITokenStorage",
]

class ITokenStorage:

    __slots__ = ()

    async def get_access_token(self) -> str:
        raise NotImplementedError()

    async def set_access_token(self, access_token: str, expire: int) -> None:
        raise NotImplementedError()

    async def get_refresh_token(self) -> str:
        raise NotImplementedError()

    async def set_refresh_token(self, refresh_token: str, expire: int) -> None:
        raise NotImplementedError()

    async def clear(self) -> None:
        raise NotImplementedError()

    class Config(BaseTokenProviderConfig):
        ...




