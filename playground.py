
import datasets 

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Cassandra
from langchain.document_loaders import TextLoader
import secret_stuff

def load_articles(n=5):
    """ Loads N articles from the 'cnn_dailymail' dataset, in streaming mode """
    dataset = datasets.load_dataset("ag_news", split="train", streaming=True)
    data = dataset.take(n)
    return [d['text'] for d in data]

articles = load_articles()
# print((articles[0]))


embedding_function = OpenAIEmbeddings(openai_api_key=secret_stuff.OAI_KEY)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.create_documents(articles)  # creates Document objects from the text in the articles
document_chunks = text_splitter.split_documents(documents) 

# print(document_chunks[0])




# embedding = OpenAIEmbeddings(openai_api_key='sk-')
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# documents = splitter.create_documents(articles)  # creates Document objects from the text in the articles
# document_chunks = splitter.split_documents(documents)  # splits the Documents into chunks


from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

# This secure connect bundle is autogenerated when you donwload your SCB, 
# if yours is different update the file name below
cloud_config= {
  'secure_connect_bundle': 'vector_db_connect/secure-connect-vector-db.zip'
}

# This token json file is autogenerated when you donwload your token, 
# if yours is different update the file name below
with open("vector_db_connect/vector_db-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
print(session)

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")

the_vectorstore = Cassandra.from_documents(
    documents=document_chunks,
    embedding=embedding_function,
    session=session,
    keyspace='vector_db_keyspace', 
    table_name='cnn_vectors'
)
# print(articles[-1]) 
query = "Carlyle Group's reputation?"
response = the_vectorstore.similarity_search(query, k=2)
# print(response)

# retrevial augmented generation
retriever = the_vectorstore.as_retriever(search_kwargs={ 'k' : 3})
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.0, model='gpt-3.5-turbo-16k', openai_api_key=secret_stuff.OAI_KEY)

qa_retriever = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type='stuff'
)
qa = qa_retriever.run(query)
print(qa)