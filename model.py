#  --------------------------------------------------------------------------------------------
# A data model in a database should be relational which means it is described by tables.
# The data describes how the data is stored and organized.
# A data model may belong to one or more schemas, usually, it just belongs to one schema
#  --------------------------------------------------------------------------------------------
from sqlalchemy import Boolean, Column, Integer, String, Float
from db_handler import Base


class Address(Base):
    """
    This is a model class. which is having the movie table structure with all the constraint
    """
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    latitude = Column(Float(), index=True, nullable=False)
    longitude = Column(Float(), index=True, nullable=False)


