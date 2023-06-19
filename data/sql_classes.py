#this approach to breaking up the code doesn't really work. You would need to build the classes with the
#declarative base and then build the tables with the engine all inside of this .py script
#This is doable, just different 


from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from conn.db import engine


class Base(DeclarativeBase):
    pass


class essences(Base):
    __tablename__ = 'essences'

    index: Mapped[int] = mapped_column(primary_key=True)
    essence: Mapped[str] = mapped_column(unique=True)
    rarity: Mapped[str]
    restricted: Mapped[bool]


class confluence(Base):
    __tablename__ = 'confluence'

    index: Mapped[int] = mapped_column(primary_key=True)
    essence1: Mapped[str]
    essence2: Mapped[str]
    essence3: Mapped[str]
    confluence: Mapped[str]
    restricted: Mapped[bool]


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
