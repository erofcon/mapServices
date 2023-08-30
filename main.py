import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.models.database import local_database, remote_database
from app.routes.city_name import router as city_name_router
from app.routes.vehicle_type import router as vehicle_type_router
from app.routes.route import router as route_router
from app.routes.transport import router as transport_router
from app.routes.background_task import router as background_task_router
from app.background_task.to_yandex_task import yandex_schedular
from app.background_task.to_gis_task import toGis_schedular

app = FastAPI()

logger.add("logs/log.log", rotation="00:00")

app.include_router(router=city_name_router)
app.include_router(router=vehicle_type_router)
app.include_router(router=route_router)
app.include_router(router=transport_router)
app.include_router(router=background_task_router)


@app.on_event('startup')
async def startup():
    await local_database.connect()
    await remote_database.connect()
    yandex_schedular.to_yandex_start()
    toGis_schedular.to_gis_start()


@app.on_event('shutdown')
async def shutdown():
    await local_database.disconnect()
    await remote_database.disconnect()
    yandex_schedular.to_yandex_shutdown()
    toGis_schedular.to_gis_shutdown()


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0'
    )
