import xml.etree.ElementTree as elTree

from app.crud import transport as transport_crud
from app.crud import nddata as nddata_crud


async def create_xml(city_id: int, clid: str) -> str:
    root = elTree.Element('tracks', clid=clid)

    transport_list = await transport_crud.get_transport_data(city_id=city_id)

    if len(transport_list) > 0:
        for i in transport_list:
            location_data = await nddata_crud.get_nddata(i.device_id)

            if location_data is not None:
                track = elTree.SubElement(root, 'track', uuid=str(i.device_id), category=i.category, route=i.route,
                                          vehicle_type=i.vehicle_type)

                elTree.SubElement(track, 'point',
                                  latitude=str(location_data.lat), longitude=str(location_data.lon),
                                  avg_speed=str(location_data.speed), direction=str(location_data.direction),
                                  time=location_data.createddatetime.utcnow().strftime('%d%m%Y:%H%M%S')
                                  )

    return elTree.tostring(root, xml_declaration=True, encoding='utf-8').decode()
