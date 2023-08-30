from fastapi import APIRouter, HTTPException, status

from app.crud import route as route_crud
from app.schemas import route as route_schemas

router = APIRouter()


@router.post('/create_route')
async def create_route(route: route_schemas.RouteCreate):
    if not await route_crud.create_route(route=route):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.post('/get_route', response_model=list[route_schemas.Route])
async def get_route():
    return await route_crud.get_routes()
