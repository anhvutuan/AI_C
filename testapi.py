import os
from dotenv import load_dotenv
load_dotenv()
print("API key:", os.getenv("OPENAI_API_KEY"))