import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()

# Load tất cả PDF trong thư mục 'data'
loader = DirectoryLoader('data/', glob="**/*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()

print(f"Loaded {len(docs)} documents.")

# Chia nhỏ tài liệu (chunking)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(docs)

print(f"Split into {len(texts)} chunks.")

# Tạo embeddings và lưu vào Chroma
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
vector_db = Chroma.from_documents(texts, embeddings, persist_directory="vector_db")

# Lưu vào ổ đĩa
vector_db.persist()

print("Embeddings đã được lưu vào Chroma DB.")