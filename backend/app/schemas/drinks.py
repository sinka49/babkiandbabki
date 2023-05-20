import uuid

from .ingridients import ingridients_schema
from .tunedModel import TunedModel


class drinks_schema(TunedModel):
    ID: uuid.UUID
    title: str



