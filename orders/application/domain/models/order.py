from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class OrderLine:
    sku: int
    quantity: int


@dataclass
class Order:
    id: str
    user_id: str
    delivery_date: datetime
    lines: List[OrderLine]

    def add_line(self, line: OrderLine):
        self.lines.append(line)

