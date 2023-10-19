from fastapi import APIRouter, HTTPException, status
from apscheduler.schedulers.base import STATE_PAUSED, STATE_RUNNING

from app.background_task.services_send_task import services_send_schedular

router = APIRouter()


@router.post('/services_send_task_pause')
async def services_send_task_pause():
    if services_send_schedular.services_send_status() == STATE_RUNNING:
        services_send_schedular.services_send_pause()

    return HTTPException(status_code=status.HTTP_200_OK, detail='task is paused')


@router.post('/services_send_task_resume')
async def services_send_task_resume():
    if services_send_schedular.services_send_status() == STATE_PAUSED:
        services_send_schedular.services_send_resume()

    return HTTPException(status_code=status.HTTP_200_OK, detail='task resumed')


@router.get('/get_services_send_task_status')
async def get_services_send_task_status():
    task_status = services_send_schedular.services_send_status()

    return task_status

# @router.post('/yandex_task_pause')
# async def yandex_task_pause():
#     if yandex_schedular.get_to_yandex_status() == STATE_RUNNING:
#         yandex_schedular.to_yandex_pause()
#
#     return HTTPException(status_code=status.HTTP_200_OK, detail='task is paused')
#
#
# @router.post('/yandex_task_resume')
# async def yandex_task_resume():
#     if yandex_schedular.get_to_yandex_status() == STATE_PAUSED:
#         yandex_schedular.to_yandex_resume()
#
#     return HTTPException(status_code=status.HTTP_200_OK, detail='task resumed')
#
#
# @router.get('/get_yandex_task_status')
# async def get_yandex_task_status():
#     task_status = yandex_schedular.get_to_yandex_status()
#
#     return task_status
#
#
# @router.post('/to_gis_task_pause')
# async def to_gis_task_pause():
#     if yandex_schedular.get_to_yandex_status() == STATE_RUNNING:
#         yandex_schedular.to_yandex_pause()
#
#     return HTTPException(status_code=status.HTTP_200_OK, detail='task is paused')
#
#
# @router.post('/to_gis_task_resume')
# async def to_gis_task_resume():
#     if yandex_schedular.get_to_yandex_status() == STATE_PAUSED:
#         yandex_schedular.to_yandex_resume()
#
#     return HTTPException(status_code=status.HTTP_200_OK, detail='task resumed')
#
#
# @router.get('/get_to_gis_task_status')
# async def get_to_gis_task_status():
#     task_status = yandex_schedular.get_to_yandex_status()
#
#     return task_status
