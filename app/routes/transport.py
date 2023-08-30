from fastapi import APIRouter, HTTPException, status

from app.crud import transport as transport_crud
from app.schemas import transport as transport_schemas

router = APIRouter()


@router.post('/create_transport')
async def create_transport(transport: transport_schemas.TransportCreate):
    if not await transport_crud.create_transport(transport=transport):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_transport', response_model=list[transport_schemas.GetTransportData])
async def get_transport():
    return await transport_crud.get_all_transport_data()
