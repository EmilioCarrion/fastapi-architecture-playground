from dependency_injector import containers, providers
from adapters.in_memory_order_repository import InMemoryOrderRepository


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

