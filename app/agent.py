import os
import aiohttp
from app.db import fetch_documents_by_president
from app.tools import fetch_registry_by_president
from dotenv import load_dotenv

load_dotenv()

OLLAMA_API_BASE = os.getenv("OLLAMA_API_BASE")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME")

async def call_llm_agent(user_query: str):
    tools = {
        "fetch_registry_by_president": lambda name: fetch_registry_by_president(name, fetch_documents_by_president)
    }


    if "president" in user_query.lower():
        for name in ["Biden", "Trump", "Obama"]:
            if name.lower() in user_query.lower():
                result = await tools["fetch_registry_by_president"](name)
                return result

    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{OLLAMA_API_BASE}/chat/completions",
            json={
                "model": OLLAMA_MODEL_NAME,
                "messages": [{"role": "user", "content": user_query}]
            }
        ) as resp:
            res_json = await resp.json()
            return res_json["choices"][0]["message"]["content"]
