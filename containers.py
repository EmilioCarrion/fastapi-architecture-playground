from dependency_injector import containers, providers
from orders.adapters import InMemoryOrderRepository


class Container(containers.DeclarativeContainer):
    # Repos
    orders_repo = providers.Singleton(
        InMemoryOrderRepository
    )


class TestContainer(containers.DeclarativeContainer):
    # Repos
    orders_repo = providers.Singleton(
        InMemoryOrderRepository
    )

