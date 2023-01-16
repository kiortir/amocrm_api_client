from ujson import loads

from amocrm_api_client.make_json_request import RequestMethod
from amocrm_api_client.models import Task, CreateTask, Page

from .AbstractRepository import AbstractRepository
from .functions import make_params

from ...models.Filters import TaskListFilter


__all__ = [
    "TasksRepository",
]


class TasksRepository(AbstractRepository):

    __slots__ = ()

    async def get_page(
        self,
        page: int = 1,
        limit: int = 250,
        filter: TaskListFilter | None = None
    ) -> Page[Task]:
        if filter is not None and not isinstance(filter, TaskListFilter):
            raise TypeError(f"LeadListFilter expected, got {type(filter)}")

        params = make_params(page=page,
                             limit=limit, filter=filter)
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/api/v4/leads",
                parameters=params,
            )
        )
        response.json["_embedded"] = response.json["_embedded"]["leads"]
        page = self._model_builder.build_model(Page[Task], response.json)
        return page

    async def get_by_id(
        self,
        id: int
    ) -> Task:
        response = await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.GET,
                path=f"/api/v4/tasks/{id}",
            )
        )
        model = self._model_builder.build_model(Task, response.json)
        return model

    async def add(self, new_task: CreateTask) -> None:
        await self._request_executor(
            lambda: self._make_request_function.request(
                method=RequestMethod.POST,
                path=f"/api/v4/tasks",
                json=[loads(new_task.json(exclude_none=True))]
            )
        )
