"""
Modelo de dados para o objeto Produto.

Define as classes que representam um produto e o gerenciamento de produtos na aplicação.
"""
import json
from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    """
    Modelo que representa um produto.

    Attributes:
        id (int): Identificador único do produto.
        nome (str): Nome do produto.
        descricao (str): Descrição do produto.
        preco (float): Preço do produto.
        categoria (str): Categoria do produto.
        tags (List[str]): Lista de tags associadas ao produto.
    """
    id: int
    nome: str
    descricao: str
    preco: float
    categoria: str
    tags: List[str]


class Products:
    """
    Classe para gerenciar uma lista de produtos.

    Attributes:
        file_products (str): Path do arquivo JSON que contém produtos pré cadastrados.
        produtos (List[Product]): Lista de objetos Product.
        contator_produto (int): Contador para atribuir IDs únicos aos produtos.

    """
    def __init__(self):
        """Inicializa a classe Products com uma lista de produtos e um contador de produtos."""
        self.file_products: str = 'app/synthetic_data/for_register_products.json'
        self.produtos: List[Product] = self.read_products()
        self.contator_produto: int = len(self.produtos) + 1

    def read_products(self):
        """
        Abre os produtos do arquivo JSON e os carrega na lista de produtos.

        Returns:
            List[Product]: Lista de produtos carregados.
        """
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
        """Atualiza a lista de produtos no arquivo JSON."""
        produtos_dict = [produto.model_dump() for produto in self.produtos]

        with open(self.file_products, 'w', encoding='utf-8') as f:
            json.dump(produtos_dict, f, ensure_ascii=False, indent=4)

    def set_product(self, nome: str, descricao: str, preco: float, categoria: str, tags: List[str]) -> Product:
        """
        Adiciona um novo produto à lista e atualiza o json com o novo produto cadastrado.

        Args:
            nome (str): Nome do produto.
            descricao (str): Descrição do produto.
            preco (float): Preço do produto.
            categoria (str): Categoria do produto.
            tags (List[str]): Lista de tags associadas ao produto.

        Returns:
            Product: O produto recém adicionado.
        """
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
        """
        Retorna a lista de todos os produtos.

        Returns:
            List[Product]: A lista de objetos Producto.
        """
        return self.produtos

    def get_product(self, id_product: int) -> List[Product]:
        """
        Busca produtos pelo ID.

        Args:
            id_product (int): ID do produto a ser buscado.

        Returns:
            List[Product]: Lista de produtos encontrados com o ID especificado.
                           Retorna uma lista vazia se nenhum produto for encontrado.
        """
        produtos_encontrados = [produto for produto in self.produtos if produto.id == id_product]
        if not produtos_encontrados:
            print(f"Produto com id {id_product} não encontrado.")
        return produtos_encontrados

    def update_product(self, id_product: int, updated_product: Product) -> Product:
        """
        Atualiza um produto com novos dados.

        Args:
            id_product (int): ID do produto a ser atualizado.
            updated_product (Product): Instância do produto com as novas informações.

        Returns:
            Product: Instância do produto atualizado.
                     Retorna None se o produto não for encontrado.
        """
        for product in self.produtos:
            if product.id == id_product:
                product.nome = updated_product.nome
                product.descricao = updated_product.descricao
                product.preco = updated_product.preco
                product.categoria = updated_product.categoria
                product.tags = updated_product.tags
                self.write_products()
                return product
        return None

    def delete_product(self, id_product: int) -> bool:
        """
        Remove um produto pelo ID.

        Args:
            id_product (int): ID do produto a ser removido.

        Returns:
            bool: Retorna True se o produto for removido com sucesso.
                  Retorna False se o produto não for encontrado.
        """
        for i, pr in enumerate(self.produtos):
            if pr.id == id_product:
                del self.produtos[i]
                self.write_products()
                return True
        return False
