import uuid

from dependency_injector.wiring import Provide, inject
from containers import Container
from orders.application.domain.ports.required.repositories import OrderRepository
from orders.application.domain.models.order import Order


@inject
def create_order(orders_repo: OrderRepository = Provide[Container.orders_repo]) -> Order:
    order = Order(str(uuid.uuid4()), [])
    orders_repo.create_order(order)
    return order
