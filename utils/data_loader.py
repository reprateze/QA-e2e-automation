import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def carregar_json(nome_arquivo: str) -> dict:
    caminho = DATA_DIR / nome_arquivo
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)