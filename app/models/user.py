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

    """
    def __init__(self):
        """Inicializa a classe Usuarios com uma lista vazia e um contador de usuários."""
        self.usuarios: List[User] = []
        self.contador_usuario: int = 1

    def set_user(self, cpf: str, nome: str, email: str, telefone: str, endereco: str, data_nascimento: str) -> User:
        """
        Adiciona um novo usuário à lista.

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
            List[Usuario]: A lista de objetos User.
        """
        return self.usuarios

    def get_user(self, id_user: int) -> List[User]:
        """
        Busca usuários pelo ID.

        Args:
            id_user (int): ID do usuário a ser buscado.

        Returns:
            List[User]: Lista de usuários encontrados com o ID especificado.
                        Retorna uma lista vazia se nenhum usuário for encontrado.
        """
        user_encontrado = [user for user in self.usuarios if user.id == id_user]
        if not user_encontrado:
            print(f"User com id {id_user} não encontrado.")
        return user_encontrado

    def update_user(self, id_user: int, updated_user: User) -> User:
        """
        Atualiza um usuário com novos dados.

        Args:
            id_user (int): ID do usuário a ser atualizado.
            updated_user (User): Instância do usuário com as novas informações.

        Returns:
            User: Instância do usuário atualizado.
                  Retorna None se o usuário não for encontrado.
        """
        for user in self.usuarios:
            if user.id == id_user:
                user.nome = updated_user.nome
                user.email = updated_user.email
                user.telefone = updated_user.telefone
                user.endereco = updated_user.endereco
                user.data_nascimento = updated_user.data_nascimento
                return user
        return None

    def delete_user(self, id_user: int) -> bool:
        """
        Remove um usuário pelo ID.

        Args:
            id_user (int): ID do usuário a ser removido.

        Returns:
            bool: Retorna True se o usuário for removido com sucesso.
                  Retorna False se o usuário não for encontrado.
        """
        for i, user in enumerate(self.usuarios):
            if user.id == id_user:
                del self.usuarios[i]
                return True
        return False
