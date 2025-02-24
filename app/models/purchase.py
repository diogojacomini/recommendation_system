from typing import List
from pydantic import BaseModel


class Purchase(BaseModel):
    id: int
    id_user: int
    id_product: int


class PurchaseOrders:

    def __init__(self):
        self.orders: List[Purchase] = []
        self.contador_purchase: int = 1

    def set_order(self, id_user: int, id_product: int) -> Purchase:
        new_order = Purchase(id=self.contador_purchase, id_user=id_user, id_product=id_product)
        self.orders.append(new_order)
        self.contador_purchase += 1
        return new_order

    def get_all_orders(self) -> List[Purchase]:
        return self.orders

    def get_order_by_user(self, id_user):
        return list(filter(lambda p: p.id_user == id_user, self.orders))

    def get_order_by_product(self, id_product):
        return list(filter(lambda p: p.id_product == id_product, self.orders))
