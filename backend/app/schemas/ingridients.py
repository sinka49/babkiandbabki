import uuid


from .tunedModel import TunedModel


class ingridients_schema(TunedModel):
    ID: uuid.UUID
    title: str



