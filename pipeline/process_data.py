import os
from dotenv import load_dotenv
from pipeline.fetch_federal_data import fetch_federal_registry_data
import aiomysql
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

async def insert_documents(docs):
    conn = await aiomysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        db=os.getenv("MYSQL_DB")
    )
    async with conn.cursor() as cur:
        for doc in docs:
            await cur.execute("""
                INSERT IGNORE INTO registry_documents 
                (title, summary, publication_date, president)
                VALUES (%s, %s, %s, %s)
            """, (
                doc.get("title"), doc.get("body"), doc.get("publication_date"),
                doc.get("president") or "Unknown"
            ))
        await conn.commit()
    conn.close()

async def run_pipeline():
    docs = await fetch_federal_registry_data()
    await insert_documents(docs)

if __name__ == "__main__":
    asyncio.run(run_pipeline())
