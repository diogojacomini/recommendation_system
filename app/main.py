"""
API de Recomendação de Produtos

Este módulo inicializa a aplicação FastAPI para fornecer recomendações de produtos.
A aplicação contém um endpoint inicial para verificar se o servidor está funcionando corretamente.

Autor: Diogo Leme Jacomini
Versão: 0.0.2
"""
from typing import Dict
from fastapi import FastAPI
import asyncio
from app.routers import user, products, purchase
from app.synthetic_data.registration import register_users_lote


MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos!"

# Criando o App
app = FastAPI()
app.include_router(user.router)
app.include_router(products.router)
app.include_router(purchase.router)


@app.on_event("startup")
async def on_startup():
    # Inicia o cadastro de usuários por minuto quando a API iniciar
    asyncio.create_task(register_users_lote())


@app.get("/")
def home() -> Dict[str, str]:
    """Iniciando o servidor"""
    return {"mensagem": MENSAGEM_HOME}
