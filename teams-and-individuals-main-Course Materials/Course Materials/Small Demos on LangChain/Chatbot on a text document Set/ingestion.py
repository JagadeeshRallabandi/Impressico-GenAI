import os

from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import pinecone


# initialize PineCone.
pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENV_REGION"],
)


# Function to put vector dataset in pinecone vector DB
def ingest_docs():
    INDEX_NAME = os.environ["INDEX_NAME"]
    print(INDEX_NAME)
    #STEP1: Load Documents
    loader = DirectoryLoader("Documents", glob="**/*.txt")
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents) }documents")


    #STEP2: Split Document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Splitted into {len(documents)} chunks")

    #STEP3: Create Embeddings
    print(f"Going to add {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(documents, embeddings, index_name=INDEX_NAME)

    print("****Loading Documents to vectorestore done ***")


# set Environment Variables and ingest Data on pinecone
if __name__ == "__main__":
    ingest_docs()
