import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests
from loguru import logger

from app.crud import city_name as city_name_crud
from .create_xml import create_xml


class ToGis:
    scheduler = AsyncIOScheduler()

    def to_gis_start(self):
        self.scheduler.add_job(self.__task, trigger='interval', seconds=20)
        self.scheduler.start()

    def to_gis_shutdown(self):
        self.scheduler.shutdown()

    def to_gis_pause(self):
        self.scheduler.pause()

    def to_gis_resume(self):
        self.scheduler.resume()

    def get_to_gis_status(self) -> int:
        return self.scheduler.state

    @staticmethod
    async def __to_gis(city_id: int, clid: str):
        try:
            xml_str = await create_xml(city_id=city_id, clid=clid)

            data = f"""compressed=0&data={xml_str}"""

            headers = {'Content-Type': 'application/x-www-form-urlencoded'}

            r = requests.post(url='http://pathfinder.2gis.com:21198', data=data, headers=headers)

            logger.info(f'to gis send with status code {r.status_code}')

        except Exception as e:
            logger.error(e)

    async def __task(self):
        tasks = []

        city_names = await city_name_crud.get_send_city_name()

        if len(city_names) > 0:
            for i in city_names:
                tasks.append(
                    asyncio.ensure_future(self.__to_gis(city_id=i.id, clid=i.clid))
                )


toGis_schedular = ToGis()