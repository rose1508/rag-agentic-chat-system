async def fetch_registry_by_president(president: str, fetch_fn):
    """
    Tool to fetch registry documents for a given president name.
    """
    documents = await fetch_fn(president)
    formatted = [
        f"Title: {title}\nDate: {date}\nSummary: {summary}"
        for (title, summary, date) in documents
    ]
    return "\n\n".join(formatted) if formatted else "No documents found."
