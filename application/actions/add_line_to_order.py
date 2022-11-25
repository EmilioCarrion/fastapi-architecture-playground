from dependency_injector.wiring import Provide, inject
from containers import Container
from application.domain.ports.required.repositories import OrderRepository
from application.domain.order import OrderLine, Order


@inject
def add_line_to_order(order_id: str, sku: int, quantity: int, orders_repo: OrderRepository = Provide[Container.orders_repo]) -> Order:
    order = orders_repo.get_order_by_id(order_id)
    order.add_line(OrderLine(sku, quantity))
    orders_repo.update_order(order)
    return order
