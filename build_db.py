# This script takes data from two excel files and populates a database with two tables
# confluence and essences. These tables can be used in other scripts to interact with 
# and build various persons.


#section for import packages
import pandas as pd
from data.sql_classes import essences, confluence, Base
from conn.db import engine
from sqlalchemy.orm import Session

def main():

    essence_list = pd.read_csv('data/essence_list.csv')
    confluence_essence = pd.read_csv('data/confluence_essence_list.csv')

    # print(essence_list)
    # print(confluence_essence)

    # Easy way to write to database but doesn't use declaritive base schemas that is useful for later down the line
    # essence_list.to_sql('essences', engine)
    # confluence_essence.to_sql('confluence', engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


    #print(CreateTableessences(.__table__).compile(dialect=postgresql.dialect()))
    #print(CreateTable(confluence.__table__).compile(dialect=postgresql.dialect()))

    with Session(engine) as session:
        essence_entry = []
        #build list of essences to write
        for index, row in essence_list.iterrows():
            # print(row)
            essence = row['Essence']
            rarity = row['Rarity']
            restricted = row['Restricted']

            entry = essences(
                 essence = essence,
                 rarity = rarity,
                 restricted = restricted
            )
            
            essence_entry.append(entry)

        confluence_entry = []
        #build list of confluent essences to write
        for index, row in confluence_essence.iterrows():
            # print(row)

            entry = confluence(
                 essence1 = row['essence1'],
                 essence2 = row['essence2'],
                 essence3 = row['essence3'],
                 confluence = row['confluence'],
                 restricted = row['restricted']
            )

            confluence_entry.append(entry)
            # print(entry.essence)

    #write stuff to the database
    try:
        session.add_all(essence_entry)
        session.commit()
    except:
        print('Essence table already built')

    try:
        session.add_all(confluence_entry)
        session.commit()
    except:
        print('Confluence table already built')



if __name__ == '__main__':
    main()