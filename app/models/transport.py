from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, Boolean

from .route import route
from .vehicle_type import vehicle_type
from .city_name import city_name

metadata = MetaData()

transport = Table(
    'transport', metadata,
    Column('id', Integer(), primary_key=True),
    Column('car_number', String(), unique=True),
    Column('imei', String(), unique=True),
    Column('description', String()),
    Column('device_id', Integer(), unique=True),
    Column('category', String(), default='s'),
    Column('route', Integer(), ForeignKey(route.c.id)),
    Column('vehicle_type', Integer(), ForeignKey(vehicle_type.c.id)),
    Column('city_name', Integer(), ForeignKey(city_name.c.id)),
    Column('send', Boolean, default=True)
)
