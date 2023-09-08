import typing
import strawberry
from conn.db import conn
from data.sql_classes import essences, confluence
from strawberry.dataloader import DataLoader
from typing import List



@strawberry.type
class Essence:
    essence: str
    rarity: str
    restricted: bool


@strawberry.type
class Confluence:
    essence1: Essence
    essence2: Essence
    essence3: Essence
    confluence: str
    restricted: bool

    # @strawberry.field
    # async def get_essence(self, info) -> Essence:
    #     essence = get_essence_by_name(self.essence1.essence)
    #     return essence

@strawberry.type
class Query:
    @strawberry.field
    async def essence(self, info, keyword: str) -> Essence:
        return await get_essence_by_name(keyword)

    @strawberry.field
    async def essence_list(self, info) -> typing.List[Essence]:
        return conn.execute(
            essences.__table__.select()
        ).fetchall()
    
    @strawberry.field
    async def get_confluence(self, info, essence1: str, essence2: str, essence3: str
    ) -> Confluence:
        confluence_row = conn.execute(
            confluence.__table__.select().where(
                confluence.__table__.c.essence1 == essence1,
                confluence.__table__.c.essence2 == essence2,
                confluence.__table__.c.essence3 == essence3,
                )
            ).fetchone()
        
        if confluence_row is None:
            # Handle the case where the confluence is not found
            return None
        
        confluence_obj = Confluence(
            essence1=await get_essence_by_name(confluence_row.essence1),
            essence2=await get_essence_by_name(confluence_row.essence2),
            essence3=await get_essence_by_name(confluence_row.essence3),
            confluence=confluence_row.confluence,
            restricted=confluence_row.restricted,
        )
        
        return confluence_obj
    
# fields for confluence essences
    @strawberry.field
    async def confluence(self, index: int) -> Confluence:
        row = conn.execute(
            confluence.__table__.select().where(confluence.__table__.c.index == index)
        ).fetchone()
        confluence_obj = Confluence(
        essence1=await get_essence_by_name(row.essence1),
        essence2=await get_essence_by_name(row.essence2),
        essence3=await get_essence_by_name(row.essence3),
        confluence=row.confluence,
        restricted=row.restricted)
        print(type(confluence_obj.essence1))
        return confluence_obj


async def load_essence(keys: List[int]) -> Essence:
    # print(keys)
    return [conn.execute(
        essences.__table__.select().where(essences.__table__.c.index == key)
    ).fetchone() for key in keys]

async def get_essence_by_name(essence_name: str) -> Essence:
    result = conn.execute(
                    essences.__table__.select().where(essences.__table__.c.essence == essence_name)
                    ).fetchone()

    if result is None:
        # Handle the case where the essence is not found in the database
        return None

    essence = Essence(
        essence=result.essence,
        rarity=result.rarity,
        restricted=result.restricted
    )

    return essence

loader = DataLoader(load_fn=load_essence)
