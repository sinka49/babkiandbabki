import uuid

from pydantic.schema import date

from .tunedModel import TunedModel


class posts_schema(TunedModel):
    ID: uuid.UUID
    user_id: uuid.UUID
    title: str
    content: str
    created_at: date



