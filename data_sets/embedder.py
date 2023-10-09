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
  print('hello')
  print(response['data'][0]['embedding'])
  return response['data'][0]['embedding']


# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()
# embeddings = OpenAIEmbeddings()
# loader = TextLoader('royalcaribbean.txt', encoding='utf-8')
# documents = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)

# embeddings = OpenAIEmbeddings()
# doc_vectors = embeddings.embed_documents([t.page_content for t in texts[:5]])





# from langchain.vectorstores.pgvector import PGVector

# CONNECTION_STRING = "postgresql+psycopg2://postgres:testing@localhost:5432/vector_db"
# COLLECTION_NAME = 'royal_vectors'

# db = PGVector.from_documents(
#     embedding=embeddings,
#     documents=texts,
#     collection_name=COLLECTION_NAME,
#     connection_string=CONNECTION_STRING,
#     )


