# this approach to breaking up the code doesn't really work. You would need
# to build the classes with the declarative base and then build the tables
# with the engine all inside of this .py script This is doable, just different

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship




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
    essence1: Mapped[str] = mapped_column(ForeignKey("essences.essence"))
    essence2: Mapped[str] = mapped_column(ForeignKey("essences.essence"))
    essence3: Mapped[str] = mapped_column(ForeignKey("essences.essence"))
    confluence: Mapped[str]
    restricted: Mapped[bool]

    essence_1 = relationship("essences", foreign_keys=[essence1])
    essence_2 = relationship("essences", foreign_keys=[essence2])
    essence_3 = relationship("essences", foreign_keys=[essence3])


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
