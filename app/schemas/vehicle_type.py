from pydantic import BaseModel


class VehicleTypeBase(BaseModel):
    vehicle_type: str


class VehicleTypeCreate(VehicleTypeBase):
    pass


class VehicleType(VehicleTypeBase):
    id: int

    class Config:
        orm_mode = True
