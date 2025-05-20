import aiomysql
import os
from dotenv import load_dotenv

load_dotenv()

async def get_db_connection():
    return await aiomysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        db=os.getenv("MYSQL_DB")
    )

async def fetch_documents_by_president(president_name: str):
    conn = await get_db_connection()
    async with conn.cursor() as cur:
        await cur.execute("""
            SELECT title, summary, publication_date
            FROM registry_documents
            WHERE president = %s
            ORDER BY publication_date DESC
            LIMIT 5
        """, (president_name,))
        result = await cur.fetchall()
    conn.close()
    return result
