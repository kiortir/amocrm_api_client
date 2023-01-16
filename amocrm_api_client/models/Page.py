from typing import Generic
from typing import List
from typing import TypeVar
from typing import Optional
from typing import Type
from typing import Any
from pydantic import Field
from pydantic.generics import GenericModel, GenericModelT

import sys


__all__ = [
    "Page",
]


T = TypeVar("T")


class Page(GenericModel, Generic[T]):
    page: int = Field(..., alias='_page')
    total_items: Optional[int] = Field(None, alias='_total_items')
    page_count: Optional[int] = Field(None, alias='_page_count')
    embedded: List[T] = Field(..., alias='_embedded')

    def __class_getitem__(cls: Type[GenericModelT], params: Type[Any] | tuple[Type[Any] | ...]) -> Type[Any]:
        created_class = super().__class_getitem__(params)
        setattr(sys.modules[created_class.__module__],
                created_class.__name__, created_class)
        return created_class
