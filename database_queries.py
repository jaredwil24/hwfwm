from data.sql_classes import essences, confluence
from conn.db import conn
from sqlalchemy import select


q = conn.execute(
    essences.__table__.select().where(essences.__table__.c.essence == 'Dark')
).fetchone()

query = select(essences.__table__.c.essence).where(essences.__table__.c.essence == 'Dark')
result = conn.execute(query).fetchone()

print((result))