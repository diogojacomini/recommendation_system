"""
Módulo de rotas para operações relacionadas aos usuários.

Este módulo define as rotas responsáveis por criar e listar usuários.
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
        usuario (Usuario): O objeto Usuario a ser cadastrado.

    Returns:
        Usuario: Um novo usuário com o ID atribuído.
    """
    return users.set_user(usuario.cpf, usuario.nome, usuario.email, usuario.telefone, usuario.endereco, usuario.data_nascimento)


@router.get("/usuarios/", response_model=List[User])
def list_users() -> List[User]:
    """
    Rota para listar todos os usuários cadastrados.

    Returns:
        List[Usuario]: Uma lista de objetos Usuario.
    """
    return users.get_users()


@router.get("/usuarios/{id_user}", response_model=List[User])
def get_user(id_user: int) -> List[User]:
    user = users.get_user(id_user)
    if not user:  # Se a lista estiver vazia
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return user


@router.put("/usuarios/{id_user}", response_model=User)
def update_user(id_user: int, updated_user: User) -> User:
    user = users.update_user(id_user, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user


@router.delete("/usuarios/{id_user}", response_model=str)
def delete_user(id_user: int) -> str:
    success = users.delete_user(id_user)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return "Usuário deletado com sucesso."
