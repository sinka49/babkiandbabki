import uuid

import sqlalchemy as sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, relationship
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
                                   nullable=False)
    ingridients = relationship("Ingridient",
                           secondary="drink_ingridients",
                           back_populates="drinks")

class Ingridient(Base):
    __tablename__ = "ingridients"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    drinks = relationship("Drink",
                               secondary="drink_ingridients",
                               back_populates="ingridients")
    values_for_ingridients = relationship("ValueForIngridient",
                               secondary="params_ingridients",
                               back_populates="ingridients")

class ValueForIngridient(Base):
    __tablename__ = "values_for_ingridients"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    is_default = Column(sqlalchemy.Boolean(), default=False)
    ingridients = relationship("Ingridient",
                               secondary="params_ingridients",
                               back_populates="values_for_ingridients")

class Drink_Ingridient(Base):
    __tablename__ = "drink_ingridients"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    drink_id = Column(sqlalchemy.ForeignKey(Drink.ID))
    ingridient_id = Column(sqlalchemy.ForeignKey(Ingridient.ID))
    blurb = Column(String, nullable=False)

class Params_Ingridients(Base):
    __tablename__ = "params_ingridients"
    ID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    params_id = Column(sqlalchemy.ForeignKey(ValueForIngridient.ID))
    ingridient_id = Column(sqlalchemy.ForeignKey(Ingridient.ID))