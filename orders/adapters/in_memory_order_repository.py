from __future__ import annotations
from orders.application.domain.ports.required.repositories import OrderRepository, OrderCriteria
from orders.application.domain.models.order import Order
from typing import Any, List


class InMemoryOrderCriteria(OrderCriteria):
    def __init__(self):
        self.filters: List[tuple[str, Any]] = []

    def pk_is(self, pk) -> InMemoryOrderCriteria:
        self.filters.append(("id", pk))
        return self

    def for_delivery_date(self, delivery_date) -> InMemoryOrderCriteria:
        self.filters.append(("delivery_date", delivery_date))
        return self


class InMemoryOrderRepository(OrderRepository):
    all = InMemoryOrderCriteria()

    def __init__(self):
        self.orders = {}

    def find(self, criteria: InMemoryOrderCriteria):
        orders = self.orders.values()
        for field, value in criteria.filters:
            filtered_orders = []
            for order in orders:
                if getattr(order, field) == value:
                    filtered_orders.append(order)
            orders = filtered_orders
        return orders

    def create_order(self, order: Order):
        self.orders[order.id] = order

    def update_order(self, order: Order):
        self.orders[order.id] = order
