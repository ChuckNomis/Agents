import qdrant_client

# Script to embed company documents into Qdrant
client = qdrant_client.QdrantClient()

# Example embedding process


def embed_documents():
    documents = ["Document 1", "Document 2"]
    client.upload_collection(
        collection_name="acme_documents",
        documents=documents
    )


if __name__ == "__main__":
    embed_documents()
