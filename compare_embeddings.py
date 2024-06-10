from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
import nltk
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el API key desde las variables de entorno
openai_api_key = os.getenv('OPENAI_API_KEY')

nltk.download('punkt')

def main():
    # Get embedding for a word.
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("apple", "iphone")
    x = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {x}")

if __name__ == "__main__":
    main()
