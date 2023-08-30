from sqlalchemy import text

from app.models.database import local_database
from app.models import city_name as city_name_model
from app.schemas import city_name as city_name_schemas


async def create_city_name(city_name: city_name_schemas.CityNameBase) -> bool:
    query = city_name_model.city_name.insert().values(
        clid=city_name.clid,
        description=city_name.description,
        send=city_name.send
    )

    try:
        return await local_database.execute(query=query)
    except Exception:
        return False


async def get_city_name() -> list[city_name_schemas.CityNames]:
    query = text(
        """
            SELECT *
            FROM city_name
        """
    )

    try:
        return await local_database.fetch_all(
            query=query
        )
    except Exception:
        return []


async def get_send_city_name() -> list[city_name_schemas.CityNames]:
    query = text(
        """
            SELECT *
            FROM city_name
            WHERE send = true
        """
    )

    try:
        return await local_database.fetch_all(
            query=query
        )
    except Exception:
        return []
