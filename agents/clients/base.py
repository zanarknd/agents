from pydantic import BaseModel
from httpx import AsyncClient as httpxClient


class AsyncClient:
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
