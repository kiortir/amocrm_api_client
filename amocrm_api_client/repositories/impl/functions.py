from typing import Any
from typing import Mapping
from typing import Optional
from typing import Union
from typing import Collection

from qsparser import stringify

from ...models.Filters import BaseFilter

__all__ = [
    "make_params",
]

def make_params(
    _with: Optional[Collection[str]] = None,
    page: int = 1,
    limit: int = 250,
    query: Optional[Union[str, int]] = None,
    filter: BaseFilter | None = None
) -> Mapping[str, Any]:
    str_with = None

    if _with is not None:
        str_with = ",".join(_with)

    if filter is not None:
        if not issubclass(BaseException, filter):
            raise ValueError("Аргумент filter должен быть типа BaseFilter")

        filter = filter.dict()


    params = {
        "with": str_with,
        "page": page,
        "limit": limit,
        "query": query,
        "filter": filter
    }

    clear_params = {k: v for k, v in params.items() if v is not None}
    return stringify(clear_params)
