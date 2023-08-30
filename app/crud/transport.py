from sqlalchemy import text

from app.models.database import local_database
from app.schemas import transport as transport_schemas
from app.models import transport as transport_model
from app.crud import nddata as nddata_crud


async def create_transport(transport: transport_schemas.TransportCreate) -> bool:
    device = await nddata_crud.get_device(transport.imei)

    if device is not None:
        query = transport_model.transport.insert().values(
            car_number=transport.car_number,
            imei=transport.imei,
            device_id=device.id,
            category='s',
            route=transport.route,
            vehicle_type=transport.vehicle_type,
            city_name=transport.city_name,
            send=transport.send
        )

        try:
            return await local_database.execute(query=query)
        except Exception:
            return False

    return False


async def get_all_transport_data() -> list[transport_schemas.GetTransportData] | None:
    query = text(
        f"""
            SELECT t.id, t.car_number, t.imei, t.device_id, t.category, r.route, vt.vehicle_type
            FROM transport t
            LEFT JOIN route r
            ON r.id = t.route
            LEFT JOIN vehicle_type vt ON vt.id = t.vehicle_type
        """
    )

    try:
        return await local_database.fetch_all(query=query)
    except Exception:
        return None


async def get_transport_data(city_id: int) -> list[transport_schemas.GetTransportData] | None:
    query = text(
        f"""
            SELECT t.id, t.car_number, t.imei, t.device_id, t.category, r.route, vt.vehicle_type
            FROM transport t
            LEFT JOIN route r
            ON r.id = t.route
            LEFT JOIN vehicle_type vt ON vt.id = t.vehicle_type
            WHERE t.city_name = {city_id}
            AND t.send = true
        """
    )

    try:
        return await local_database.fetch_all(query=query)
    except Exception:
        return None
