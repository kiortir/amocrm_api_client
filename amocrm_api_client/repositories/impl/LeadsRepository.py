from typing import Collection
from typing import Optional
from typing import Union

from amocrm_api_client.make_json_request import RequestMethod
from amocrm_api_client.models import AddNote
from amocrm_api_client.models import CreateLead
from amocrm_api_client.models import Lead
from amocrm_api_client.models import Page
from amocrm_api_client.models import UpdateLead

from .AbstractRepository import AbstractRepository
from .functions import make_params
from ..core import IPaginable
from ...models.Filters import LeadListFilter


__all__ = [
    "LeadsRepository",
]


class LeadsRepository(IPaginable[Lead], AbstractRepository):

    __slots__ = ()

    async def get_page(
        self,
        _with: Optional[Collection[str]] = None,
        page: int = 1,
        limit: int = 250,
        query: Optional[Union[str, int]] = None,
        filter: LeadListFilter | None = None,
    ) -> Page[Lead]:
        if filter is not None and not isinstance(filter, LeadListFilter):
            raise TypeError(f"LeadListFilter expected, got {type(filter)}")

        params = make_params(_with=_with, page=page, limit=limit, query=query, filter=filter)
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/api/v4/leads",
                parameters=params,
            )
        )
        response.json["_embedded"] = response.json["_embedded"]["leads"]
        page = self._model_builder.build_model(Page[Lead], response.json)
        return page

    async def get_by_id(
        self,
        id: int,
        _with: Optional[Collection[str]] = None
    ) -> Lead:
        params = make_params(_with=_with)
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/api/v4/leads/{id}",
                parameters=params,
            )
        )
        model = self._model_builder.build_model(Lead, response.json)
        return model

    async def add(self, new_lead: CreateLead) -> None:
        await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.POST,
                path=f"/api/v4/leads",
                json=[new_lead.dict(by_alias=True, exclude_none=True)]
            )
        )

    async def update(self, lead: UpdateLead) -> None:
        await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.PATCH,
                path=f"/api/v4/leads",
                json=[lead.dict(by_alias=True, exclude_none=True)]
            )
        )

    async def updates(self, leads: Collection[UpdateLead]) -> None:
        await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.PATCH,
                path=f"/api/v4/leads",
                json=[lead.dict(by_alias=True, exclude_none=True) for lead in leads]
            )
        )

    async def add_notes(self, notes: Collection[AddNote]) -> None:
        await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.POST,
                path=f"/api/v4/leads/notes",
                json=[note.dict(exclude_none=True) for note in notes]
            )
        )
