from pydantic import BaseModel


class RouteBase(BaseModel):
    route: str
    city_id: int


class RouteCreate(RouteBase):
    pass


class Route(RouteBase):
    id: int

    class Config:
        orm_mode = True
