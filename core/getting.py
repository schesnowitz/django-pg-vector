from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()


loader = TextLoader("./royal.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

CONNECTION_STRING = "postgresql+psycopg2://postgres:testing@localhost:5432/vector_db"
COLLECTION_NAME = 'clapton_vectors'

db = PGVector(
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    embedding_function=embeddings,
)


# query = "what should I wear?"
# docs_with_score = db.similarity_search_with_score(query)

# for doc, score in docs_with_score:
#     print("-" * 80)
#     print("Score: ", score)
#     print(doc.page_content)
#     print("-" * 80)

query = "what about my medications?"
# response = db.similarity_search(query)
# retriever = db.as_retriever()
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.0, model='gpt-3.5-turbo-16k')

# qa_retriever = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever,
#     chain_type='stuff'
# )
# qa = qa_retriever.run(query)
# print(qa)


prompt_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}

Instructions: {instructions}:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question", "instructions"],
)


def run_retrieval_qa_pipeline(text, instructions='', k=2):
    partial_prompt = PROMPT.partial(instructions=instructions)
    retriever = db.as_retriever(search_kwargs={'k': k})

    chain_type_kwargs = { 'prompt' : partial_prompt}
    qa_retriever = RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs=chain_type_kwargs
    )
    # print(embeddings)  
    # res = qa_retriever.run(text)
    # print(text)
    # print(res)
    return qa_retriever.run(text)


print(run_retrieval_qa_pipeline("when was he born?", 'every response needs to end with "crazy good times!"'))