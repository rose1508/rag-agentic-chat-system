import aiohttp

async def fetch_federal_registry_data():
    url = "https://www.federalregister.gov/api/v1/documents.json"
    params = {"per_page": 10, "order": "newest"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()
            return data["results"]
