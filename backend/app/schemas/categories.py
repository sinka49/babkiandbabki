import uuid

from pydantic.schema import List

from .tunedModel import TunedModel


class categories_schema(TunedModel):
    ID: uuid.UUID
    parrent_category: uuid.UUID
    title: str



