from typing import Any
from typing import Mapping
from typing import Type

from amocrm_api_client.make_json_request import MakeJsonRequestFunctionImpl

from .StandardTokenProvider import StandardTokenProvider
from ..GetTokensByAuthCodeFunction import GetTokensByAuthCodeFunction
from ..GetTokensByRefreshTokenFunction import GetTokensByRefreshTokenFunction
from ...core import ITokenProvider

from .token_storage import TokenStorageImpl, ITokenStorage

__all__ = [
    "StandardTokenProviderFactory",
]


class StandardTokenProviderFactory:
    __slots__ = ()

    def get_instance(
        self,
        settings: Mapping[str, Any],
        token_storage_class: Type[ITokenStorage] = TokenStorageImpl,
        **kwargs
    ) -> ITokenProvider:
        config = token_storage_class.Config(**settings)
        print((config.dict() | kwargs))
        token_storage = token_storage_class(**(config.dict() | kwargs))

        make_json_request_function = MakeJsonRequestFunctionImpl()

        get_tokens_by_auth_code_function = GetTokensByAuthCodeFunction(
            make_json_request_function=make_json_request_function,
        )

        get_tokens_by_refresh_token_function = (
            GetTokensByRefreshTokenFunction(
                make_json_request_function=make_json_request_function,
            )
        )

        token_provider = StandardTokenProvider(
            config=config,
            get_tokens_by_auth_code=get_tokens_by_auth_code_function,
            get_tokens_by_refresh_token=get_tokens_by_refresh_token_function,
            token_storage=token_storage,
        )

        return token_provider
