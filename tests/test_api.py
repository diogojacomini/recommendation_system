from typing import Dict, List
import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_home():
    """
    Test the home endpoint.
    Ensures that the API returns a welcome message.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'mensagem': 'Bem-vindo à API de Recomendação de Produtos!'}


# region Test Users

def test_user_create():
    """
    Test creating a new user.
    Ensures that the API correctly registers a new user with valid data.
    """
    user_test: Dict[str, str] = {
        "id": 1,
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


def test_user_list():
    """
    Test retrieving all users.
    Ensures that the API returns the list of registered users.
    """
    response = client.get('/usuarios/')
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_user_update():
    """
    Test updating an existing user.
    Ensures that the API successfully updates a user's details.
    """
    updated_user: Dict[str, str] = {
        "id": 1,
        "cpf": "test_update",
        "nome": "Usuario de Teste Alter",
        "email": "test.user@email.com",
        "telefone": "(11)999999991",
        "endereco": "rua teste numero test",
        "data_nascimento": "1991/02/20"
    }
    response = client.put('/usuarios/1', json=updated_user)
    assert response.status_code == 200
    assert response.json()['cpf'] == 'test_'
    assert response.json()['nome'] == updated_user['nome']
    assert response.json()['email'] == 'test.user@email.com'


def test_user_get():
    """
    Test retrieving a specific user.
    Ensures that the API returns correct user details for a given ID.
    """
    response = client.get('/usuarios/1')
    assert response.status_code == 200
    assert isinstance(response.json()[0]['id'], int) and response.json()[0]['id'] == 1
    assert isinstance(response.json()[0]['cpf'], str) and response.json()[0]['cpf'] == 'test_'
    assert isinstance(response.json()[0]['nome'], str) and response.json()[0]['nome'] == 'Usuario de Teste Alter'


def test_user_delete():
    """
    Test deleting a user.
    Ensures that the API successfully deletes a user by ID.
    """
    response = client.delete('/usuarios/1')
    assert response.status_code == 200


def test_user_get_nonexistent():
    """
    Test retrieving a non-existent user.
    Ensures that the API returns a 404 status code.
    """
    response = client.get('/usuarios/1')
    assert response.status_code == 404

# endregion user


# region Test Products
def test_product_create():
    """
    Test creating a new product.
    Ensures that the API correctly registers a new product with valid data.
    """
    product_test: Dict[str, str | float | List] = {
        "id": 2148,
        "nome": "Produto de Teste",
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


def test_product_list():
    """
    Test retrieving all registered products.
    Ensures that the API returns the correct number of products based on stored data.
    """
    response = client.get('/produtos/')
    with open('app/synthetic_data/for_register_products.json', 'r', encoding='utf-8') as f:
        produtos_rw = json.load(f)
    assert response.status_code == 200
    assert len(response.json()) == len(produtos_rw)


def test_product_update():
    """
    Test updating an existing product.
    Ensures that the API successfully updates a product's details.
    """
    updated_product = {"id": 134,
                       "nome": "Produto de Teste Alterado",
                       "descricao": "produto de teste",
                       "preco": 10.99,
                       "categoria": "test",
                       "tags": ["test1", "test2"]}

    response = client.put('/produtos/13', json=updated_product)
    assert response.status_code == 200
    assert response.json()['id'] == 13
    assert response.json()['nome'] == updated_product['nome']
    assert response.json()['preco'] == updated_product['preco']
    assert len(response.json()['tags']) == 2


def test_product_get():
    """
    Test retrieving all products.
    Ensures that the API returns the expected number of products.
    """
    response = client.get('/produtos/13')
    assert response.status_code == 200
    assert isinstance(response.json()[0]['id'], int) and response.json()[0]['id'] == 13
    assert isinstance(response.json()[0]['nome'], str) and response.json()[0]['nome'] == 'Produto de Teste Alterado'


def test_product_delete():
    """
    Test deleting a product.
    Ensures that the API successfully deletes a product by ID.
    """
    response = client.delete('/produtos/13')
    assert response.status_code == 200


def test_product_get_nonexistent():
    """
    Test retrieving a non-existent product.
    Ensures that the API returns a 404 status code.
    """
    response = client.get('/produtos/13')
    assert response.status_code == 404

# endregion Test Products
