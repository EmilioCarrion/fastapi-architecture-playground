from dependency_injector.wiring import Provide, inject
from containers import Container
from orders.application.domain.ports.required.repositories import OrderRepository
from orders.application.domain.models.order import Order
from typing import List


@inject
def get_all_orders(orders_repo: OrderRepository = Provide[Container.orders_repo]) -> List[Order]:
    return orders_repo.find(service_date=)
