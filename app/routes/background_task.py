from fastapi import APIRouter, HTTPException, status
from apscheduler.schedulers.base import STATE_PAUSED, STATE_RUNNING

from app.background_task.to_yandex_task import yandex_schedular

router = APIRouter()


@router.post('/yandex_task_pause')
async def yandex_task_pause():
    if yandex_schedular.get_to_yandex_status() == STATE_RUNNING:
        yandex_schedular.to_yandex_pause()

    return HTTPException(status_code=status.HTTP_200_OK, detail='task is paused')


@router.post('/yandex_task_resume')
async def yandex_task_resume():
    if yandex_schedular.get_to_yandex_status() == STATE_PAUSED:
        yandex_schedular.to_yandex_resume()

    return HTTPException(status_code=status.HTTP_200_OK, detail='task resumed')


@router.get('/get_yandex_task_status')
async def get_yandex_task_status():
    task_status = yandex_schedular.get_to_yandex_status()

    return task_status


@router.post('/to_gis_task_pause')
async def to_gis_task_pause():
    if yandex_schedular.get_to_yandex_status() == STATE_RUNNING:
        yandex_schedular.to_yandex_pause()

    return HTTPException(status_code=status.HTTP_200_OK, detail='task is paused')


@router.post('/to_gis_task_resume')
async def to_gis_task_resume():
    if yandex_schedular.get_to_yandex_status() == STATE_PAUSED:
        yandex_schedular.to_yandex_resume()

    return HTTPException(status_code=status.HTTP_200_OK, detail='task resumed')


@router.get('/get_to_gis_task_status')
async def get_to_gis_task_status():
    task_status = yandex_schedular.get_to_yandex_status()

    return task_status
