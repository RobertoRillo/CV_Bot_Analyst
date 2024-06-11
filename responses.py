from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el API key desde las variables de entorno
openai_api_key = os.getenv('OPENAI_API_KEY')
CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Responde la pregunta basado en este contexto:

{context}

Eres un bot que responde preguntas acerca del reglamento de tránsito de Jalisco. Responde como un robot asistente, y si te preguntan algo fuera del contexto responde que para eso no fuiste programado.

Responde la pregunta basado en el contexto de arriba: {question}
"""

def get_response(user_input: str) -> str:
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    
    # Buscar en la base de datos
    results = db.similarity_search_with_relevance_scores(user_input, k=3)
    if len(results) == 0 or results[0][1] < 0.3:
        return "Unable to find matching results."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=user_input)
    
    model = ChatOpenAI(api_key=openai_api_key)
    response_text = model.invoke(prompt)
    
    # Solo retornar la respuesta del modelo
    return response_text
