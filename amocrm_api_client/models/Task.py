from datetime import (
    datetime
)

from pydantic import (
    BaseModel
)


__all__ = [
    "Task",
    "CreateTask"
]


class TaskResult(BaseModel):
    text: str


class BaseTask(BaseModel):
    responsible_user_id: int | None = None
    entity_id: int | None = None
    entity_type: str | None = None
    task_type_id: int | None = None
    text: str
    duration: int | None = None
    complete_till: datetime
    result: TaskResult | None = None

    created_at: datetime | None = None
    updated_at: datetime | None = None


class Task(BaseTask):
    id: int
    created_by: int | None = None
    updated_by: int | None = None
    group_id: int | None = None
    duration: int | None = None
    is_completed: bool | None = None
    task_type_id: int | None = None
    account_id: int | None = None


class CreateTask(BaseTask):
    request_id: str | None = None

    class Config:
        json_encoders = {
            datetime: lambda v: int(v.timestamp()),
        }
