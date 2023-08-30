from fastapi import APIRouter, HTTPException, status

from app.crud import city_name as city_names_crud
from app.schemas import city_name as city_name_schemas

router = APIRouter()


@router.post('/create_city_name')
async def create_city_name(city_name: city_name_schemas.CityNameCreate):
    if not await city_names_crud.create_city_name(city_name=city_name):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_city_name', response_model=list[city_name_schemas.CityNames])
async def get_city_name():
    return await city_names_crud.get_city_name()
