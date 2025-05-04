from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from src.inventory_item import InventoryItem
from services.inventory_item_service import InventoryItemService
from repositories.inmemory.inventory_item_repository import InMemoryInventoryItemRepository


class InventoryItemSchema(BaseModel):
    item_id: str
    name: str
    quantity: int
    price: float
    status: str  


class InventoryUpdateSchema(BaseModel):
    quantity: Optional[int] = None
    status: Optional[str] = None

repo = InMemoryInventoryItemRepository()
service = InventoryItemService(repo)

router = APIRouter(prefix="/api/inventory", tags=["Inventory"])

def to_schema(item: InventoryItem) -> InventoryItemSchema:
    return InventoryItemSchema(
        item_id=item.get_item_id(),
        name=item.get_name(),
        quantity=item.get_quantity(),
        price=item.get_price(),
        status=item.get_status(),
    )

@router.get("/", response_model=List[InventoryItemSchema])
def list_items():
    return [to_schema(i) for i in service.list_items()]

@router.post("/", response_model=InventoryItemSchema)
def create_item(item: InventoryItemSchema):
    obj = InventoryItem(
        item_id=item.item_id,
        name=item.name,
        quantity=item.quantity,
        price=item.price,
        status=item.status,
    )
    return to_schema(service.add_item(obj))

@router.put("/{item_id}", response_model=InventoryItemSchema)
def update_item(item_id: str, updated: InventoryItemSchema):
    obj = InventoryItem(
        item_id=updated.item_id,
        name=updated.name,
        quantity=updated.quantity,
        price=updated.price,
        status=updated.status,
    )
    result = service.update_item(item_id, obj)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return to_schema(result)

@router.patch("/{item_id}/restock", response_model=InventoryItemSchema)
def restock_item(item_id: str, quantity: int):
    item = service.restock_item(item_id, quantity)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return to_schema(item)

@router.patch("/{item_id}/mark-out-of-stock", response_model=InventoryItemSchema)
def mark_out_of_stock(item_id: str):
    item = service.mark_out_of_stock(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return to_schema(item)
