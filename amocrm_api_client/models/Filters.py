from pydantic import BaseModel, Field


class RangeFilterValues(BaseModel):

    from_field: int = Field(..., alias='from')
    to: int


class BareBoneFilter(BaseModel):
    id: int | list[int] | None = None
    responsible_user_id: int | list[int] | None = None
    updated_at: int | RangeFilterValues | None = None


class BaseFilter(BareBoneFilter):

    name: str | list[str] | None = None

    created_by: int | list[int] | None = None
    updated_by: int | list[int] | None = None

    created_at: RangeFilterValues | None = None

    closest_task_at: RangeFilterValues | None = None

    custom_fields_values: dict | None = None


class StatusFilterEntry(BaseFilter):

    pipeline_id: int | None = None
    status_id: int | None = None


class LeadListFilter(BaseFilter):

    price: RangeFilterValues | None = None
    statuses: list[StatusFilterEntry] | None = None
    pipeline_id: int | list[int] | None = None


class CompanyListFilter(BaseFilter):
    ...


class TaskListFilter(BareBoneFilter):
    is_completed: bool | None
    task_type: int | list[int] | None
    entity_type: str | None


class CustomersListFilter(BaseFilter):

    next_price: str | list[str] | None = None
    next_date: RangeFilterValues | None = None
    status_id: int | list[int] | None = None
