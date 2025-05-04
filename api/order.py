# api/order.py

from fastapi import APIRouter, HTTPException
from datetime import datetime
from src.order import Order
from services.order_service import OrderService
from repositories.inmemory.order_repository import InMemoryOrderRepository
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api/order", tags=["Orders"])

# Pydantic schemas
class OrderItem(BaseModel):
    name: str
    price: float
    quantity: int

class OrderRequest(BaseModel):
    order_id: str
    status: str
    date: datetime
    items: List[OrderItem] = []

class OrderResponse(BaseModel):
    order_id: str
    status: str
    date: datetime
    total_amount: float
    items: List[OrderItem]

# In-memory service instance
service = OrderService(InMemoryOrderRepository())

def to_schema(order: Order) -> OrderResponse:
    return OrderResponse(
        order_id=order.get_order_id(),
        status=order.get_status(),
        date=order.date,
        total_amount=order.get_total_amount(),
        items=[
            OrderItem(name=item.name, price=item.price, quantity=item.quantity)
            for item in order.get_items()
        ],
    )

@router.post("/", response_model=OrderResponse, tags=["Orders"])
def create_order(req: OrderRequest):
    order = Order(order_id=req.order_id, status=req.status, date=req.date)
    for item in req.items:
        order.add_item(item)
    return to_schema(service.create_order(order))

@router.get("/{order_id}", response_model=OrderResponse, tags=["Orders"])
def get_order(order_id: str):
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return to_schema(order)

@router.get("/", response_model=List[OrderResponse], tags=["Orders"])
def list_orders():
    return [to_schema(order) for order in service.list_orders()]

@router.delete("/{order_id}", tags=["Orders"])
def delete_order(order_id: str):
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    service.delete_order(order_id)
    return {"message": f"Order {order_id} deleted successfully"}

