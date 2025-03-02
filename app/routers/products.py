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


@router.get("/produtos/{id_product}", response_model=List[Product])
def list_product(id_product: int) -> List[Product]:
    produtos = products.get_product(id_product)
    if not produtos:
        raise HTTPException(status_code=404, detail=f"Produto '{id_product}' não encontrado")
    return produtos


@router.put("/produtos/{id_product}", response_model=Product)
def update_product(id_product: int, updated_product: Product) -> Product:
    product = products.update_product(id_product, updated_product)
    if not product:
        raise HTTPException(status_code=404, detail=f"Produto '{id_product}' não encontrado")
    return product


@router.delete("/produtos/{id_product}", response_model=str)
def delete_product(id_product: int) -> str:
    success = products.delete_product(id_product)
    if not success:
        raise HTTPException(status_code=404, detail=f"Produto '{id_product}' não encontrado")
    return f"Produto '{id_product}' deletado com sucesso."
