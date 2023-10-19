from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String

from .city_name import city_name

metadata = MetaData()

route = Table(
    'route', metadata,
    Column('id', Integer(), primary_key=True),
    Column('route', String(), unique=True),
    Column('description', String()),
    Column('city_id', Integer(), ForeignKey(city_name.c.id, ondelete='CASCADE'))
)
