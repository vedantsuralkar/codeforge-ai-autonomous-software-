
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.documents import Document


# ==========================================
# VECTOR STORE
# ==========================================

class VectorMemory:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vectorstore = None

    # ======================================
    # CREATE EMBEDDINGS AND STORE
    # ======================================

    def create_vector_store(self, texts):

        documents = [
            Document(page_content=text)
            for text in texts
        ]

        self.vectorstore = FAISS.from_documents(
            documents,
            self.embeddings
        )

        return "Vector database created successfully!"

    # ======================================
    # ADD NEW DOCUMENTS
    # ======================================

    def add_documents(self, texts):

        if self.vectorstore is None:
            return self.create_vector_store(texts)

        documents = [
            Document(page_content=text)
            for text in texts
        ]

        self.vectorstore.add_documents(documents)

        return "Documents added successfully!"

    # ======================================
    # SIMILARITY SEARCH
    # ======================================

    def search_memory(self, query, k=3):

        if self.vectorstore is None:
            return []

        results = self.vectorstore.similarity_search(
            query,
            k=k
        )

        return [
            document.page_content
            for document in results
        ]

    # ======================================
    # SAVE VECTOR DATABASE
    # ======================================

    def save_vector_store(self, path="memory/faiss_index"):

        if self.vectorstore is None:
            return "Vector database is empty!"

        self.vectorstore.save_local(path)

        return "Vector database saved successfully!"

    # ======================================
    # LOAD VECTOR DATABASE
    # ======================================

    def load_vector_store(self, path="memory/faiss_index"):

        self.vectorstore = FAISS.load_local(
            path,
            self.embeddings,
            allow_dangerous_deserialization=False
        )

        return "Vector database loaded successfully!"


# ==========================================
# CREATE VECTOR MEMORY OBJECT
# ==========================================

vector_memory = VectorMemory()
