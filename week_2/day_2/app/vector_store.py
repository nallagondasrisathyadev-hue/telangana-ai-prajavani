import chromadb
from chromadb.config import Settings

class GovSchemeVectorStore:
    def __init__(self, persist_dir: str = "./data/chroma_db"):
        self.chroma_client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.chroma_client.get_or_create_collection(name="telangana_schemes")

    def seed_policy_document(self, doc_id: str, text: str, metadata: dict):
        """Encodes and saves public government schema context boundaries securely inside our database memory."""
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )

    def query_matching_schemes(self, query_text: str, n_results: int = 2) -> dict:
        """Queries localized matching baseline context boundaries to patch agent execution frames."""
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )

if __name__ == "__main__":
    store = GovSchemeVectorStore()
    store.seed_policy_document(
        doc_id="SCHEME-001",
        text="Rythu Bandhu investment support scheme provides financial aid to farmers directly per acre every crop season.",
        metadata={"department": "Revenue", "target": "Farmers"}
    )
    print("Vector storage persistent system engine successfully seeded.")
