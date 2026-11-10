"""Cliente LLM compartido: el mismo SDK de OpenAI sirve para OpenAI y para Ollama."""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVEEDOR = os.getenv("PROVEEDOR", "ollama")  # "ollama" (gratis, local) u "openai"

if PROVEEDOR == "openai":
    cliente = OpenAI()  # lee OPENAI_API_KEY del .env
    MODELO = os.getenv("MODELO", "gpt-6-luna")
else:
    cliente = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    MODELO = os.getenv("MODELO", "qwen2.5-coder:7b")
