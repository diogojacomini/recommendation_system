from typing import List
from fastapi import APIRouter
from app.models.purchase import Purchase, PurchaseOrders

router = APIRouter()
orders: PurchaseOrders = PurchaseOrders()


@router.post("/purchase/", response_model=Purchase)
def create_product(order: Purchase) -> Purchase:
    return orders.set_order(order.id_user, order.id_product)


@router.get("/purchase/", response_model=List[Purchase])
def list_products() -> List[Purchase]:
    return orders.get_all_orders()


@router.get("/historico_user/{usuario_id}", response_model=List[Purchase])
def historico_compras(usuario_id: int) -> List[Purchase]:
    """
    Adiciona ou atualiza o histórico de compras de um usuário.

    Args:
        usuario_id (int): O ID do usuário para o qual o histórico de compras será atualizado.
        compras (HistoricoCompras): O objeto contendo os IDs dos produtos comprados.

    Returns:
        dict: Mensagem indicando que o histórico de compras foi atualizado.
    """
    return orders.get_order_by_user(usuario_id)
