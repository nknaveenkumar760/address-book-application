#  --------------------------------------------------------------------------------
# A schema is a collection of database objects that are logically grouped together.
# These can be anything, tables, views, stored procedure etc.
# Schemas are typically used to logically group objects in a database.
#  ---------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    pass


class AddressAdd(AddressBase):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class Address(AddressAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
