from __future__ import annotations
from orders.application.domain.ports.required.repositories import OrderRepository, Equals, Not, Criteria
from orders.application.domain.models.order import Order
from typing import Any, List


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def find(self, *criteria_list: Criteria):
        orders = self.orders.values()
        for criteria in criteria_list:
            orders = self._apply_criteria(orders, criteria)
        return orders

    def _apply_criteria(self, orders: List[Order], criteria: Criteria):
        if isinstance(criteria, Equals):
            return list(filter(lambda x: getattr(x, criteria.field) == criteria.value, orders))
        if isinstance(criteria, Not):
            excluded = self._apply_criteria(orders, criteria.criteria)
            return [order for order in orders if order not in excluded]
        return orders

    def create_order(self, order: Order):
        self.orders[order.id] = order

    def update_order(self, order: Order):
        self.orders[order.id] = order
