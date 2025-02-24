from typing import List
from fastapi import APIRouter, HTTPException
from app.models.products import Product, Products

router = APIRouter()
products: Products = Products()


@router.post("/produtos/", response_model=Product)
def create_product(produto: Product) -> Product:
    return products.set_product(produto.nome,
                                produto.descricao,
                                produto.preco,
                                produto.categoria,
                                produto.tags)


@router.get("/produtos/", response_model=List[Product])
def list_products() -> List[Product]:
    return products.get_products()


@router.get("/produtos/{id_producto}", response_model=List[Product])
def list_product(id_producto: int) -> List[Product]:
    produtos = products.get_product(id_producto)
    if not produtos:  # Se a lista estiver vazia
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produtos
