from typing import Any
from typing import Mapping
from typing import Optional
from typing import Union
from typing import Collection


__all__ = [
    "make_params",
]


def make_params(
    _with: Optional[Collection[str]] = None,
    page: int = 1,
    limit: int = 250,
    query: Optional[Union[str, int]] = None,
    filter: dict | None = None
) -> Mapping[str, Any]:
    str_with = None

    if _with is not None:
        str_with = ",".join(_with)


    params = {
        "with": str_with,
        "page": page,
        "limit": limit,
        "query": query,
    }


    if filter is not None:
        filter_params = {f"filter[{k}]": v for k, v in filter.items()}
        params.update(filter_params)

    clear_params = {k: v for k, v in params.items() if v is not None}
    return clear_params
