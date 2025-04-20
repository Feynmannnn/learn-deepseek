import os
from openai import OpenAI

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
DEEPSEEK_REASONER_MODEL = "deepseek-reasoner"
DEEPSEEK_CHAT_MODEL = "deepseek-chat"

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,  
    base_url=DEEPSEEK_BASE_URL
)