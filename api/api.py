import typing
import strawberry
from conn.db import conn
from data.sql_classes import essences
from sqlalchemy import select


@strawberry.type
class Essence:
    essence: str
    rarity: str
    restricted: bool


@strawberry.type
class Confluence:
    essence1: str
    essence2: str
    essence3: str
    confluence: str
    restricted: bool


@strawberry.type
class Query:
    @strawberry.field
    def essence(self, info, index: int) -> Essence:
        return conn.execute(
            essences.__table__.select().where(essences.__table__.c.index == index)
            ).fetchone()

    @strawberry.field
    def essence_list(self, info) -> typing.List[Essence]:
        return conn.execute(
            essences.__table__.select()
            ).fetchall()
