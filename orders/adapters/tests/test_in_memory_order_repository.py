import uuid

import pytest
from datetime import datetime, timedelta
from orders.adapters.in_memory_order_repository import InMemoryOrderRepository
from orders.conftest import OrderFactory


class TestInMemoryOrderRepository:
    @pytest.fixture
    def repo(self):
        return InMemoryOrderRepository()

    def test_returns_all_orders(self, repo):
        repo.create_order(OrderFactory())
        repo.create_order(OrderFactory())

        assert len(repo.find(repo.all)) == 2

    def test_returns_today_orders(self, repo):
        today = datetime.now().date()
        tomorrow = (datetime.now() + timedelta(days=1)).date()
        repo.create_order(OrderFactory(delivery_date=today))
        repo.create_order(OrderFactory(delivery_date=tomorrow))

        assert len(repo.find(repo.all.for_delivery_date(today))) == 1

    def test_returns_order_with_given_id(self, repo):
        order_id = uuid.uuid4()
        repo.create_order(OrderFactory(id=order_id))
        repo.create_order(OrderFactory())

        orders = repo.find(repo.all.pk_is(order_id))
        assert len(orders) == 1
        assert orders[0].id == order_id
