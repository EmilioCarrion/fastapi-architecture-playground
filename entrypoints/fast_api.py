from fastapi import FastAPI
from dependency_injector.wiring import Provide, inject
from application import actions
from pydantic import BaseModel
from typing import List
from containers import Container

app = FastAPI()


container = Container()
container.init_resources()
container.wire(modules=[
    'application.actions.add_line_to_order',
    'application.actions.create_order',
    'application.actions.get_all_orders',
])


class OrderLine(BaseModel):
    sku: int
    quantity: int


class Order(BaseModel):
    id: str
    lines: List[OrderLine]


@app.post("/orders", response_model=Order)
async def create_order():
    order = actions.create_order()
    return order


@app.get("/orders", response_model=List[Order])
async def get_orders():
    return actions.get_all_orders()


@app.post("/orders/{uuid}/lines", response_model=Order)
async def add_line(uuid: str, sku: int, quantity: int):
    order = actions.add_line_to_order(uuid, sku, quantity)
    return order


