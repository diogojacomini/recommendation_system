import json
from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    categoria: str
    tags: List[str]


class Products:

    def __init__(self):
        self.file_products = 'app/synthetic_data/for_register_products.json'
        self.produtos: List[Product] = self.read_products()
        self.contator_produto: int = len(self.produtos) + 1

    def read_products(self):
        with open(self.file_products, 'r', encoding='utf-8') as f:
            produtos_rw = json.load(f)

        ls_product_fmt: List[Product] = []
        for produto in produtos_rw:
            ls_product_fmt.append(Product(id=produto.get('id'),
                                          nome=produto.get('nome'),
                                          descricao=produto.get('descricao'),
                                          preco=produto.get('preco'),
                                          categoria=produto.get('categoria'),
                                          tags=produto.get('tags')))

        return ls_product_fmt

    def write_products(self):
        produtos_dict = [produto.model_dump() for produto in self.produtos]

        with open(self.file_products, 'w', encoding='utf-8') as f:
            json.dump(produtos_dict, f, ensure_ascii=False, indent=4)

    def set_product(self, nome: str, descricao: str, preco: float, categoria: str, tags: List[str]) -> Product:
        novo_produto = Product(id=self.contator_produto,
                               nome=nome,
                               descricao=descricao,
                               preco=preco,
                               categoria=categoria,
                               tags=tags)

        self.produtos.append(novo_produto)
        self.contator_produto += 1
        self.write_products()
        return novo_produto

    def get_products(self) -> List[Product]:
        return self.produtos

    def get_product(self, id_producto: int) -> List[Product]:
        produtos_encontrados = [produto for produto in self.produtos if produto.id == id_producto]
        if not produtos_encontrados:
            print(f"Produto com id {id_producto} não encontrado.")
        return produtos_encontrados
