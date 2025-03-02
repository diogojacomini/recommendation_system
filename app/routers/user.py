"""
Módulo de rotas para operações relacionadas aos usuários.

Este módulo define as rotas responsáveis por criar e listar, pesquisar, atualizar e excluir usuários.
"""
from typing import List
from fastapi import APIRouter, HTTPException
from app.models.user import User, Users

router = APIRouter()
users: Users = Users()


@router.post("/usuarios/", response_model=User)
def create_user(usuario: User) -> User:
    """
    Rota para cadastrar usuários.

    Args:
        usuario (User): O objeto User a ser cadastrado.

    Returns:
        Usuario: Um novo usuário com o ID atribuído.
    """
    return users.set_user(usuario.cpf, usuario.nome, usuario.email, usuario.telefone, usuario.endereco, usuario.data_nascimento)


@router.get("/usuarios/", response_model=List[User])
def list_users() -> List[User]:
    """
    Rota para listar todos os usuários cadastrados.

    Returns:
        List[User]: Uma lista de objetos Usuario.
    """
    return users.get_users()


@router.get("/usuarios/{id_user}", response_model=List[User])
def get_user(id_user: int) -> List[User]:
    """
    Rota para listar usuários pelo ID.

    Args:
        id_user (int): ID do usuário a ser listado.

    Returns:
        List[User]: Lista de usuários encontrados com o ID especificado.

    Raises:
        HTTPException: Se nenhum usuário for encontrado, uma exceção HTTP 404 é levantada com a mensagem "Usuário '{id_user}' não encontrado".
    """
    user = users.get_user(id_user)
    if not user:
        raise HTTPException(status_code=404, detail=f"Usuário '{id_user}' não encontrado")
    return user


@router.put("/usuarios/{id_user}", response_model=User)
def update_user(id_user: int, updated_user: User) -> User:
    """
    Rota para atualizar um usuário existente.

    Args:
        id_user (int): ID do usuário a ser atualizado.
        updated_user (User): Instância do usuário com as novas informações.

    Returns:
        User: Instância do usuário atualizado.

    Raises:
        HTTPException: Se o usuário não for encontrado, uma exceção HTTP 404 é levantada com a mensagem "Usuário '{id_user}' não encontrado".
    """
    user = users.update_user(id_user, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail=f"Usuário '{id_user}' não encontrado")
    return user


@router.delete("/usuarios/{id_user}", response_model=str)
def delete_user(id_user: int) -> str:
    """
    Rota para deletar um usuário pelo ID.

    Args:
        id_user (int): ID do usuário a ser deletado.

    Returns:
        str: Mensagem de sucesso se o usuário for deletado.

    Raises:
        HTTPException: Se o usuário não for encontrado, uma exceção HTTP 404 é levantada com a mensagem "Usuário '{id_product}' não encontrado".
    """
    success = users.delete_user(id_user)
    if not success:
        raise HTTPException(status_code=404, detail=f"Usuário '{id_user}' não encontrado")
    return f"Usuário '{id_user}' deletado com sucesso."
