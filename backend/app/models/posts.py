import uuid


import sqlalchemy
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from .Base import Base
from .users import users_table

metadata = Base.metadata


class Post(Base):
    __tablename__ = "posts"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column("ID", sqlalchemy.ForeignKey(users_table.c.id)),
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=sqlalchemy.DateTime())
