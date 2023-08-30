from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean

metadata = MetaData()

city_name = Table(
    'city_name', metadata,
    Column('id', Integer(), primary_key=True),
    Column('clid', String(), unique=True),
    Column('description', String()),
    Column('send', Boolean, default=True)
)
