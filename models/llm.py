


def load_openai():

    try:
        return ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model="gpt-4o-mini"
        )

    except Exception as e:
        print(e)


def load_gemini():

    try:
        return ChatGoogleGenerativeAI(
            google_api_key=GEMINI_API_KEY,
            model="gemini-pro"
        )

    except Exception as e:
        print(e)


def load_groq():

    try:
        return ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama3-8b-8192"
        )

    except Exception as e:
        print(e)