"""
Modelo de dados para o objeto Usuario.

Define as classes que representam um usuário e o gerenciamento de usuários na aplicação.
"""
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    """
    Modelo que representa um usuário com ID e nome.

    Attributes:
        id (int): Identificador único do usuário.
        cpf (str): Identificaor usuário CPF.
        nome (str): Nome do usuário.
        email (str): Email do usuário.
        telefone (str): Telefone do usuário.
        endereço (str): Endereço do usuário.
        data_nascimento (str): Data de nascimento do usuário no padrão "yyyy-mm-dd"
    """
    id: int
    cpf: str
    nome: str
    email: str
    telefone: str
    endereco: str
    data_nascimento: str


class Users:
    """
    Classe para gerenciar uma lista de usuários.

    Attributes:
        usuarios (List[Usuario]): Lista de objetos Usuario.
        contador_usuario (int): Contador para atribuir IDs únicos aos usuários.

    Methods:
        set_usuario(nome: str) -> Usuario:
            Adiciona um novo usuário à lista e retorna o objeto Usuario criado.

        get_usuarios() -> List[Usuario]:
            Retorna a lista de todos os usuários cadastrados.
    """
    def __init__(self):
        """Inicializa a classe Usuarios com uma lista vazia e um contador de usuários."""
        self.usuarios: List[User] = []
        self.contador_usuario: int = 1

    def set_user(self, cpf: str, nome: str, email: str, telefone: str, endereco: str, data_nascimento: str) -> User:
        """
        Adiciona um novo usuário à lista de usuários.

        Args:
            cpf (str): Identificaor usuário CPF.
            nome (str): Nome do usuário.
            email (str): Email do usuário.
            telefone (str): Telefone do usuário.
            endereço (str): Endereço do usuário.
            data_nascimento (str): Data de nascimento do usuário no padrão "yyyy-mm-dd"

        Returns:
            Usuario: O objeto Usuario criado com o ID atribuído.
        """
        novo_usuario = User(id=self.contador_usuario,
                            cpf=cpf,
                            nome=nome,
                            email=email,
                            telefone=telefone,
                            endereco=endereco,
                            data_nascimento=data_nascimento)

        self.usuarios.append(novo_usuario)
        self.contador_usuario += 1
        return novo_usuario

    def get_users(self) -> List[User]:
        """
        Retorna a lista de todos os usuários cadastrados.

        Returns:
            List[Usuario]: A lista de objetos Usuario.
        """
        return self.usuarios
