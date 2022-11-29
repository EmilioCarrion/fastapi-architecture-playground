import factory
from datetime import datetime
from orders.application.domain.models.order import Order


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    id = factory.Faker('uuid4')
    user_id = factory.Faker('uuid4')
    delivery_date = datetime.now().date()
    lines = []
