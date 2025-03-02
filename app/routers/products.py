"""
Módulo de rotas para operações relacionadas aos produtos.

Este módulo define as rotas responsáveis por criar e listar, pesquisar, atualizar e excluir produtos.
"""
from typing import List
from fastapi import APIRouter, HTTPException
from app.models.products import Product, Products

router = APIRouter()
products: Products = Products()


@router.post("/produtos/", response_model=Product)
def create_product(produto: Product) -> Product:
    """
    Rota para cadastrar produtos.

    Args:
        usuario (Product): O objeto Product a ser cadastrado.

    Returns:
        Product: Um novo produto com o ID atribuído.
    """
    return products.set_product(produto.nome,
                                produto.descricao,
                                produto.preco,
                                produto.categoria,
                                produto.tags)


@router.get("/produtos/", response_model=List[Product])
def list_products() -> List[Product]:
    """
    Rota para listar todos os produtos cadastrados.

    Returns:
        List[Product]: Uma lista de objetos Product.
    """
    return products.get_products()


@router.get("/produtos/{id_product}", response_model=List[Product])
def get_product(id_product: int) -> List[Product]:
    """
    Rota para listar produtos pelo ID.

    Args:
        id_product (int): ID do produto a ser listado.

    Returns:
        List[Product]: Lista de produtos encontrados com o ID especificado.

    Raises:
        HTTPException: Se nenhum produto for encontrado, uma exceção HTTP 404 é levantada com a mensagem "Produto '{id_product}' não encontrado".
    """
    produtos = products.get_product(id_product)
    if not produtos:
        raise HTTPException(status_code=404, detail=f"Produto '{id_product}' não encontrado")
    return produtos


@router.put("/produtos/{id_product}", response_model=Product)
def update_product(id_product: int, updated_product: Product) -> Product:
    """
    Rota para atualizar um produto existente.

    Args:
        id_product (int): ID do produto a ser atualizado.
        updated_product (Product): Instância do produto com as novas informações.

    Returns:
        Product: Instância do produto atualizado.

    Raises:
        HTTPException: Se o produto não for encontrado, uma exceção HTTP 404 é levantada com a mensagem "Produto '{id_product}' não encontrado".
    """
    product = products.update_product(id_product, updated_product)
    if not product:
        raise HTTPException(status_code=404, detail=f"Produto '{id_product}' não encontrado")
    return product


@router.delete("/produtos/{id_product}", response_model=str)
def delete_product(id_product: int) -> str:
    """
    Rota para deletar um produto pelo ID.

    Args:
        id_product (int): ID do produto a ser deletado.

    Returns:
        str: Mensagem de sucesso se o produto for deletado.

    Raises:
        HTTPException: Se o produto não for encontrado, uma exceção HTTP 404 é levantada com a mensagem "Produto '{id_product}' não encontrado".
    """
    success = products.delete_product(id_product)
    if not success:
        raise HTTPException(status_code=404, detail=f"Produto '{id_product}' não encontrado")
    return f"Produto '{id_product}' deletado com sucesso."
