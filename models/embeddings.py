from langchain.embeddings import HuggingFaceEmbeddings


def load_embedding_model():

    try:

        model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        return model

    except Exception as e:
        print(e)