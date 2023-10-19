import asyncio
import time

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
from loguru import logger

from app.crud import city_name as city_name_crud
from .create_xml import create_xml


class ServicesSend:
    scheduler = AsyncIOScheduler()

    def services_send_start(self):
        self.scheduler.add_job(self.__task, trigger='interval', seconds=20)
        self.scheduler.start()

    def services_send_shutdown(self):
        self.scheduler.shutdown()

    def services_send_pause(self):
        self.scheduler.pause()

    def services_send_resume(self):
        self.scheduler.resume()

    def services_send_status(self) -> int:
        return self.scheduler.state

    @staticmethod
    async def __services_send(city_id: int, clid: str):

        xml_str = await create_xml(city_id=city_id, clid=clid)

        # print(xml_str)
        if xml_str is None:
            logger.info(f'transport list is empty')
            return

        data = f"""compressed=0&data={xml_str}""".encode()

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        try:
            r = requests.post(url='http://extjams.maps.yandex.net/mtr_collect/1.x/', data=data, headers=headers, timeout=5)
            logger.info(f'to yandex send with status code {r.status_code}')
        except Exception as e:
            logger.error(e)
        time.sleep(1)
        try:
            r = requests.post(url='http://pathfinder.2gis.com:21198', data=data, headers=headers, timeout=5)
            logger.info(f'to gis send with status code {r.status_code}')
        except Exception as e:
            logger.error(e)

    async def __task(self):
        tasks = []

        city_names = await city_name_crud.get_send_city_name()

        if len(city_names) > 0:
            for i in city_names:
                tasks.append(
                    asyncio.ensure_future(self.__services_send(city_id=i.id, clid=i.clid))
                )


services_send_schedular = ServicesSend()
