from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS


from models.embeddings import load_embedding_model



def create_vector_store(file_path):

    try:

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(documents)

        embedding_model = load_embedding_model()

        vector_store = FAISS.from_documents(
            chunks,
            embedding_model
        )

        return vector_store

    except Exception as e:
        print(e)