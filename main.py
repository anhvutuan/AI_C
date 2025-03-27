import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import tiktoken
from tiktoken.load import load_tiktoken_bpe
from tiktoken.core import Encoding

# Load environment variables from .env file
load_dotenv()

# Force tiktoken to use local encoding file
local_tiktoken_path = os.path.expanduser("~/.cache/tiktoken/cl100k_base.tiktoken")

mergeable_ranks = load_tiktoken_bpe(local_tiktoken_path)
encoding = Encoding(
    name="cl100k_base",
    pat_str=r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""",
    mergeable_ranks=mergeable_ranks,
    special_tokens={
        "<|endoftext|>": 100257,
        "<|fim_prefix|>": 100258,
        "<|fim_middle|>": 100259,
        "<|fim_suffix|>": 100260
    }
)

# Override tiktoken encoding_for_model function
def encoding_for_model(model_name):
    return encoding

tiktoken.encoding_for_model = encoding_for_model

# Hàm OCR + lưu hình ảnh không trích xuất được text
def extract_text_with_ocr(pdf_path, output_image_dir="images/"):
    doc = fitz.open(pdf_path)
    all_text = ""

    os.makedirs(output_image_dir, exist_ok=True)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Trích xuất text trực tiếp (nếu có)
        text = page.get_text()
        if text.strip():
            all_text += f"\n--- Page {page_num+1} (text) ---\n{text}"
            continue

        # Nếu không có text -> OCR
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        ocr_text = pytesseract.image_to_string(img, lang='eng+vie')

        if ocr_text.strip():
            all_text += f"\n--- Page {page_num+1} (OCR) ---\n{ocr_text}"
        else:
            # Lưu hình ảnh không thể OCR
            img_path = os.path.join(output_image_dir, f"{os.path.basename(pdf_path)}_page_{page_num+1}.png")
            img.save(img_path)
            print(f"[!] Page {page_num+1} of '{pdf_path}' saved to {img_path} for manual check.")

    return all_text

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
