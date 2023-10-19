import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.models.database import local_database, remote_database
from app.routes.city_name import router as city_name_router
from app.routes.vehicle_type import router as vehicle_type_router
from app.routes.route import router as route_router
from app.routes.transport import router as transport_router
from app.routes.background_task import router as background_task_router
from app.background_task.services_send_task import services_send_schedular

app = FastAPI()

logger.add("/mnt/projects_files/mapServices/logs/log.log", rotation="00:00", enqueue=True)

app.include_router(router=city_name_router)
app.include_router(router=vehicle_type_router)
app.include_router(router=route_router)
app.include_router(router=transport_router)
app.include_router(router=background_task_router)


@app.on_event('startup')
async def startup():
    await local_database.connect()
    await remote_database.connect()
    services_send_schedular.services_send_start()


@app.on_event('shutdown')
async def shutdown():
    await local_database.disconnect()
    await remote_database.disconnect()
    services_send_schedular.services_send_shutdown()


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0'
    )
