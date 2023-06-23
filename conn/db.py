from sqlalchemy import create_engine, MetaData

# DEFINE THE DATABASE CREDENTIALS
user = 'postgres'
host = '127.0.0.1'
password = None
port = 5432
database = 'hwfwm'
if password is None:
    engine = create_engine(
        f'postgresql+psycopg2://{user}@{host}:{port}/{database}'
        )
else:
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
        )

meta = MetaData()
conn = engine.connect()
