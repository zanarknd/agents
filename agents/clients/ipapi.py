from pydantic import BaseModel
from urllib.parse import urljoin

from clients.base import AsyncClient

API_URL = "http://ip-api.com/json/"

# {
#     "status": "success",
#     "country": "Cyprus",
#     "countryCode": "CY",
#     "region": "02",
#     "regionName": "Limassol District",
#     "city": "Limassol",
#     "zip": "",
#     "lat": 34.6874,
#     "lon": 33.0366,
#     "timezone": "Asia/Nicosia",
#     "isp": "Superdach LTD",
#     "org": "Real",
#     "as": "AS206912 Superdach LTD",
#     "query": "185.170.235.227",
# }


class IpApiReponse(BaseModel):
    lat: float
    lon: float

    country: str
    countryCode: str
    regionName: str
    city: str
    zip: str


class IpApiClient(AsyncClient):
    async def get_geo_data(self, ip: str | None = None):
        path = "/json/"
        if ip:
            path = urljoin(path, ip)
        return await self._request("GET", path, IpApiReponse)
