


st.title("NeoStats Chatbot")


mode = st.radio(
    "Response Mode",
    ["Concise", "Detailed"]
)



uploaded_file = st.file_uploader(
    "Upload document",
    type=["pdf"]
)


vectorstore = None


if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    vectorstore = create_vector_store("temp.pdf")


query = st.text_input("Ask a question")


if query:

    llm = load_openai()

    context = ""

    if vectorstore:

        docs = vectorstore.similarity_search(query)
        context = docs[0].page_content

    else:

        context = web_search(query)


    if mode == "Concise":

        prompt = f"""
        Answer briefly.

        Context:
        {context}

        Question:
        {query}
        """

    else:

        prompt = f"""
        Provide detailed explanation.

        Context:
        {context}

        Question:
        {query}
        """


    response = llm.invoke(prompt)

    st.write(response.content)