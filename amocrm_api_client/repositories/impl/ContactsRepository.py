from typing import Collection, Optional, Union

from amocrm_api_client.make_json_request import RequestMethod

from amocrm_api_client.models import Page
from amocrm_api_client.models import Contact

from ..core import IPaginable
from .AbstractRepository import AbstractRepository
from ...models.Filters import CustomersListFilter


from .functions import make_params


__all__ = [
    "ContactsRepository",
]


class ContactsRepository(IPaginable[Contact], AbstractRepository):

    __slots__ = ()

    async def get_page(
        self,
        _with: Optional[Collection[str]] = None,
        page: int = 1,
        limit: int = 250,
        query: Optional[Union[str, int]] = None,
        filter: CustomersListFilter | None = None,
    ) -> Page[Contact]:
        if filter is not None and not isinstance(filter, CustomersListFilter):
            raise TypeError(
                f"CustomersListFilter expected, got {type(filter)}")
        params = make_params(_with=_with, page=page, limit=limit, query=query, filter=filter)
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/api/v4/contacts",
                parameters=params,
            )
        )

        response.json["_embedded"] = response.json["_embedded"]["contacts"]
        model = self._model_builder.build_model(
            model_type=Page[Contact],
            data=response.json,
        )
        return model

    async def get_by_id(
        self,
        id: int
    ) -> Contact:
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/api/v4/contacts/{id}",
            )
        )
        model = self._model_builder.build_model(Contact, response.json)
        return model

    async def smart_redirect(self, phone: str) -> Collection[Contact]:
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/private/api/v2/json/contacts/list",
                parameters={"query": phone}
            )
        )

        result = []
        for json_contact in response.json["response"]["contacts"]:
            result.append(self._model_builder.build_model(Contact, json_contact))

        return result
