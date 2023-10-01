import openai
import tiktoken
from django.conf import settings
EMBEDDING_MODEL = "text-embedding-ada-002"

def embed_input(text):
  text = text.replace('\n', " ")
  response = openai.Embedding.create(
    input=[text],
    model=EMBEDDING_MODEL,
    api_key=settings.OPENAI_API_KEY
    )
  # print(response)
  return response['data'][0]['embedding']
