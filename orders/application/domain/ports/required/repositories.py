from __future__ import annotations
from abc import ABC
from orders.application.domain.models.order import Order
from typing import Any, List


class Criteria(ABC):
    pass


class Equals(Criteria):
    def __init__(self, field, value):
        self.field = field
        self.value = value


class Not(Criteria):
    def __init__(self, criteria):
        self.criteria = criteria


class OrderRepository(ABC):
    def find(self, *args: Criteria) -> List[Order]: ...
    def create_order(self, order: Order): ...
    def update_order(self, order: Order): ...
