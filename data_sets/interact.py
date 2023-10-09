from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain.vectorstores import PGEmbedding

load_dotenv()
embeddings = OpenAIEmbeddings()



from langchain.vectorstores.pgvector import PGVector

CONNECTION_STRING = "postgresql+psycopg2://postgres:testing@localhost:5432/vector_db"
# COLLECTION_NAME = 'royal_vectors'
def search_for_vectors(texts):
  db = PGEmbedding.from_documents(
      embedding=embeddings,
      documents=texts,
      collection_name='test driver',
      connection_string=CONNECTION_STRING,
      )

  # question = "what kind of clothes should I wear?"

  # search = db.similarity_search_with_relevance_scores(query=question, k=2)

  # print(len(search))
