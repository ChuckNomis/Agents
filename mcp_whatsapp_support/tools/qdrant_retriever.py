import qdrant_client

# Qdrant RAG retriever
client = qdrant_client.QdrantClient()


def retrieve_documents(query):
    results = client.search_collection(
        collection_name="acme_documents",
        query=query
    )
    return results
