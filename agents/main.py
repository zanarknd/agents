import asyncio
from pydantic_ai import Agent
from settings import settings
from clients.ipapi import IpApiClient


class GeminiModels:
    flash = "gemini-2.5-flash"
    flash_lite = "gemini-2.5-flash-lite"


agent = Agent(GeminiModels.flash_lite, instructions="Be concise, answer with one sentence.")


async def main():
    # result = agent.run_sync("What will the weather be tomorrow in the city where I am?")
    # print(result)

    ip_api_client = IpApiClient(host=settings.clients.ipapi.host, user_agent=settings.user_agent)

    print(await ip_api_client.get_geo_data())
    print(await ip_api_client.get_geo_data("8.8.8.8"))


if __name__ == "__main__":
    asyncio.run(main())
