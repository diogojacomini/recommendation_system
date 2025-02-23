"""
Este módulo contém funções para gerar dados sintéticos de usuários, como CPF, nome,
email, telefone, endereço e data de nascimento, utilizando a biblioteca Faker para
os dados pessoais e gerando um CPF válido aleatório.

As funções principais incluem:
- `generate_user()`: Gera um dicionário com dados sintéticos de uma pessoa.
- `generate_cpf()`: Gera um CPF válido aleatório.
- `post_register_user()`: Envia uma requisição assíncrona para cadastrar uma pessoa na API.
- `register_users_lote()`: Simula o cadastro de várias pessoas a cada minuto, enviando as requisições de forma assíncrona.
"""
from typing import Dict
from random import randint
from datetime import datetime
import asyncio
from faker import Faker
import httpx

fake = Faker()


def generate_user() -> Dict[str, str]:
    """
    Gera um dicionário contendo informações aleatórias de um usuário.

    Utiliza a biblioteca Faker para gerar dados como nome, e-mail, telefone,
    endereço e data de nascimento, além de gerar um CPF "válido" de forma aleatória.

    Retorna:
        Dict[str, str]: Um dicionário contendo os dados da pessoa gerada, incluindo:
                         'id' (int), 'cpf' (str), 'nome' (str), 'email' (str),
                         'telefone' (str), 'endereco' (str), 'data_nascimento' (str).
    """
    return {"id": 2148,
            "cpf": generate_cpf(),
            "nome": fake.name(),
            "email": fake.email(),
            "telefone": fake.phone_number(),
            "endereco": fake.address().replace("\n", " "),
            "data_nascimento": fake.date_of_birth(minimum_age=18).strftime('%Y-%m-%d')
            }


def generate_cpf():
    """
    Gera um número de CPF válido de forma aleatória.

    Utiliza a fórmula de validação do CPF para gerar dois dígitos verificadores
    e garantir que o CPF gerado seja válido dentro do sistema de validação.

    Retorna:
        str: O número de CPF gerado, no formato 'XXXXXXXXXXX'.
    """
    numeros = [randint(0, 9) for _ in range(9)]  # Gerando os 9 primeiros dígitos aleatórios

    # Calculando o primeiro dígito verificador
    soma1 = sum([(10 - i) * numeros[i] for i in range(9)])
    digito1 = (soma1 * 10) % 11
    if digito1 in (10, 11):
        digito1 = 0

    # Calculando o segundo dígito verificador
    soma2 = sum([(11 - i) * numeros[i] for i in range(9)]) + (2 * digito1)
    digito2 = (soma2 * 10) % 11
    if digito2 in (10, 11):
        digito2 = 0

    return ''.join(map(str, numeros)) + str(digito1) + str(digito2)


async def post_register_user(client, pessoa):
    """
    Envia uma requisição POST assíncrona para cadastrar uma pessoa.

    Utiliza o cliente HTTP assíncrono (httpx) para enviar os dados da pessoa gerada
    para a API em um formato JSON.

    Args:
        client (httpx.AsyncClient): O cliente HTTP assíncrono para realizar a requisição.
        pessoa (Dict[str, str]): Um dicionário contendo os dados da pessoa a ser cadastrada.

    Retorna:
        httpx.Response: A resposta da requisição, contendo o status da operação.
    """
    url = "http://127.0.0.1:8000/usuarios/"
    response = await client.post(url, json=pessoa)
    return response


async def register_users_lote():
    """
    Simula o cadastro de múltiplas pessoas a cada minuto, realizando uma requisição assíncrona.

    A cada intervalo de tempo aleatório, entre 1 e 60 segundos, o script irá gerar
    entre 1 e n novas pessoas e enviá-las para a API. O número de pessoas geradas por
    vez e o intervalo de tempo são aleatórios.

    A função continuará rodando em loop até que seja interrompida manualmente.

    """
    async with httpx.AsyncClient() as client:
        while True:
            qtd_new_users = randint(1, 5)
            tasks = [post_register_user(client, generate_user()) for _ in range(qtd_new_users)]
            await asyncio.gather(*tasks)
            print(f"{qtd_new_users} pessoas cadastradas às {datetime.now()}")
            await asyncio.sleep(randint(1, 60))  # Espera de 60 segundos para o próximo lote
