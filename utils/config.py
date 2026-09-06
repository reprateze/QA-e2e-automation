import os

from dotenv import load_dotenv

load_dotenv()

FIXED_USER_EMAIL = os.getenv("FIXED_USER_EMAIL")
FIXED_USER_PASSWORD = os.getenv("FIXED_USER_PASSWORD")

_api_base_url = os.getenv("API_BASE_URL")
if not _api_base_url:
    raise RuntimeError(
        "API_BASE_URL não definido. Crie um arquivo .env na raiz do projeto "
        "com API_BASE_URL=<url> (veja o README)."
    )
API_BASE_URL = _api_base_url.strip()