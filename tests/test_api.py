from typing import Dict, List
import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'mensagem': 'Bem-vindo à API de Recomendação de Produtos!'}


def test_start_products():
    response = client.get('/produtos/')
    assert response.status_code == 200
    assert len(response.json()) == 12


def test_first_product():
    response = client.get('/produtos/1')
    assert response.status_code == 200
    assert response.json()[0]['id'] == 1
    assert response.json()[0]['nome'] == 'Samsung Galaxy S23'
    assert response.json()[0]['categoria'] == 'Smartphones'


def test_create_product():
    product_test: Dict[str, str | float | List] = {
        "id": 2148,
        "nome": "test_",
        "descricao": "produto de teste",
        "preco": 0.99,
        "categoria": "test",
        "tags": ["test1", "test2", "testapi"]
    }
    response = client.post('/produtos/', json=product_test)
    assert response.status_code == 200
    assert response.json()['nome'] == product_test['nome']
    assert response.json()['descricao'] == product_test['descricao']
    assert response.json()['preco'] == product_test['preco']
    assert response.json()['categoria'] == product_test['categoria']
    assert response.json()['tags'] == product_test['tags']
    assert len(response.json()['tags']) == 3


def test_listar_produtos():
    response = client.get('/produtos/')
    with open('app/synthetic_data/for_register_products.json', 'r', encoding='utf-8') as f:
        produtos_rw = json.load(f)
    assert response.status_code == 200
    assert len(response.json()) == len(produtos_rw)


def test_criar_usuario():
    user_test: Dict[str, str] = {
        "id": 2148,
        "cpf": "test_",
        "nome": "Usuario de Teste",
        "email": "test.user@email.com",
        "telefone": "(11)999999999",
        "endereco": "rua teste numero test",
        "data_nascimento": "1991/02/20"
    }
    response = client.post('/usuarios/', json=user_test)
    assert response.status_code == 200
    assert response.json()['cpf'] == user_test['cpf']
    assert response.json()['nome'] == user_test['nome']
    assert response.json()['data_nascimento'] == user_test['data_nascimento']


def test_listar_users():
    response = client.get('/usuarios/')
    assert response.status_code == 200


def test_listar_user():
    response = client.get('/usuarios/1')
    assert response.status_code == 200
    assert isinstance(response.json()[0]['id'], int)
    assert isinstance(response.json()[0]['cpf'], str)
    assert isinstance(response.json()[0]['nome'], str)
    assert isinstance(response.json()[0]['data_nascimento'], str)
