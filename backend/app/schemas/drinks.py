import uuid

from pydantic.schema import List

from .ingridients import ingridients_schema
from .tunedModel import TunedModel


class drinks_schema(TunedModel):
    ID: uuid.UUID
    title: str
    is_active_constructor: bool = True
    ingridients: List[ingridients_schema] = None

    class Config:
        orm_mode = True


