from __future__ import annotations
from orders.application.domain.ports.required.repositories import OrderRepository, Equals, Not, Criteria
from orders.application.domain.models.order import Order
from typing import Any, List, Type, Union


def handle_equals(criteria: Equals, orders: List[Order]):
    return list(filter(lambda x: getattr(x, criteria.field) == criteria.value, orders))


def handle_not(criteria: Not, orders: List[Order]):
    handler = CRITERIA_HANDLERS[criteria.criteria]
    excluded = handler(criteria.criteria, orders)
    return [order for order in orders if order not in excluded]


CRITERIA_HANDLERS = {
    Equals: handle_equals,
    Not: handle_not
}


AcceptedCriteria = Union[Equals, Not]


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def find(self, *criteria_list: AcceptedCriteria):
        orders = self.orders.values()
        for criteria in criteria_list:
            orders = self._apply_criteria(orders, criteria)
        return orders

    @staticmethod
    def _apply_criteria(orders: List[Order], criteria: AcceptedCriteria):
        handler = CRITERIA_HANDLERS[type(criteria)]
        return handler(criteria, orders)

    def create_order(self, order: Order):
        self.orders[order.id] = order

    def update_order(self, order: Order):
        self.orders[order.id] = order
