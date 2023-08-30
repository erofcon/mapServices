from fastapi import APIRouter, HTTPException, status

from app.schemas import vehicle_type as vehicle_type_schemas
from app.crud import vehicle_type as vehicle_type_crud

router = APIRouter()


@router.post('/create_vehicle_type')
async def create_vehicle_type(vehicle_type: vehicle_type_schemas.VehicleTypeCreate):
    if not await vehicle_type_crud.create_vehicle_type(vehicle_type=vehicle_type):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_vehicle_type', response_model=list[vehicle_type_schemas.VehicleType])
async def get_vehicle_type():
    return await vehicle_type_crud.get_vehicle_type()
