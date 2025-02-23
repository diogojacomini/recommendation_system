"""
API de Recomendação de Produtos

Este módulo inicializa a aplicação FastAPI para fornecer recomendações de produtos.
A aplicação contém um endpoint inicial para verificar se o servidor está funcionando corretamente.

Autor: Diogo Leme Jacomini
Versão: 0.0.2
"""
from typing import Dict
from fastapi import FastAPI
from app.routers import user

MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos!"

# Criando o App
app = FastAPI()
app.include_router(user.router)


@app.get("/")
def home() -> Dict[str, str]:
    """Iniciando o servidor"""
    return {"mensagem": MENSAGEM_HOME}
