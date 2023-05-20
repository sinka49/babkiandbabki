import uuid

import sqlalchemy as sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

metadata = sqlalchemy.MetaData()
class Category(Base):
    __tablename__ = "categories"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    parrent_category = Column(sqlalchemy.ForeignKey('categories.ID'), index=True, nullable=True)

class Drink(Base):
    __tablename__ = "drinks"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(sqlalchemy.ForeignKey(Category.ID)),
    title = Column(String, nullable=False)
    is_active_constructor = Column(sqlalchemy.Boolean(),
                                   server_default=sqlalchemy.sql.expression.true(),
                                   nullable=False )
class Ingridient(Base):
    __tablename__ = "ingridients"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

class Drink_Ingridient(Base):
    __tablename__ = "drink_ingridients"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Column('drink_id', sqlalchemy.ForeignKey(Drink.ID), primary_key=True),
    Column('ingridient_id', sqlalchemy.ForeignKey(Ingridient.ID), primary_key=True)

