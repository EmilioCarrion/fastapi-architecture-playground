from dataclasses import dataclass
from typing import List


@dataclass
class OrderLine:
    sku: int
    quantity: int


@dataclass
class Order:
    id: str
    lines: List[OrderLine]

    def add_line(self, line: OrderLine):
        self.lines.append(line)

