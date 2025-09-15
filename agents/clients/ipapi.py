from pydantic import BaseModel
from httpx import AsyncClient as httpxClient
from urllib.parse import urljoin

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


class IpApiClient:
    def __init__(self, host: str, user_agent: str | None = None):
        headers = {}
        if user_agent:
            headers["user-agent"] = user_agent

        self.client = httpxClient(base_url=host, headers=headers)

    async def _request(self, method: str, path: str, response_model: BaseModel | None = None):
        response = await self.client.request(method, path)
        if not response.status_code == 200:
            response.raise_for_status()

        if response_model:
            return response_model.model_validate_json(response.text)
        else:
            return response

    async def get_geo_data(self, ip: str | None = None):
        path = "/json/"
        if ip:
            path = urljoin(path, ip)
        return await self._request("GET", path, IpApiReponse)
