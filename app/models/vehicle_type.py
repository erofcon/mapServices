from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

vehicle_type = Table(
    'vehicle_type', metadata,
    Column('id', Integer(), primary_key=True),
    Column('vehicle_type', String(), unique=True),
)
