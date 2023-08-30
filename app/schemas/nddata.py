from datetime import datetime
from pydantic import BaseModel


class NddataDevice(BaseModel):
    id: int


class Nddata(BaseModel):
    id: int
    createddatetime: datetime
    deviceid: int
    lat: float
    lon: float
    speed: float
    direction: float
