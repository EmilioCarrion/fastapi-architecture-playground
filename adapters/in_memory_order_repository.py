from application.domain.ports.required.repositories import OrderRepository
from application.domain.order import Order
from typing import List


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def get_order_by_id(self, order_id: str) -> Order:
        return self.orders.get(order_id)

    def get_all_orders(self) -> List[Order]:
        return list(self.orders.values())

    def create_order(self, order: Order):
        self.orders[order.id] = order

    def update_order(self, order: Order):
        self.orders[order.id] = order
