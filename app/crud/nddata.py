from datetime import datetime, timedelta
from sqlalchemy import text

from app.models.database import remote_database
from app.schemas import nddata as nddata_schemas


async def get_device(imei: str) -> nddata_schemas.NddataDevice | None:
    query = text(f"""
        SELECT id
        FROM navigationdevice
        WHERE code = '{imei}'
        AND isdeleted = '0'
    """)

    try:
        return await remote_database.fetch_one(query=query)
    except Exception:
        return None


async def get_nddata(device_id: int) -> nddata_schemas.Nddata | None:
    query = text(f"""
        SELECT id, createddatetime, lat, lon, speed, direction
        FROM nddata
        WHERE deviceid = {device_id}
        AND createddatetime > '{datetime.now() - timedelta(minutes=5)}'
        ORDER BY createddatetime DESC LIMIT 1
    """)

    try:
        return await remote_database.fetch_one(query=query)

    except Exception:
        return None
