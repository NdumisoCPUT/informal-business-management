from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from src.cash_flow_entry import CashFlowEntry
from services.cash_flow_entry_service import CashFlowService
from repositories.inmemory.cash_flow_entry_repository import InMemoryCashFlowEntryRepository

# Main schema
class CashFlowEntrySchema(BaseModel):
    entry_id: str
    amount: float
    entry_type: str
    status: str
    date: datetime

# Partial update schema
class CashFlowEntryUpdateSchema(BaseModel):
    amount: Optional[float] = None
    entry_type: Optional[str] = None
    status: Optional[str] = None
    date: Optional[datetime] = None

repo = InMemoryCashFlowEntryRepository()
service = CashFlowService(repo)

router = APIRouter(prefix="/api/cashflow", tags=["Cash Flow"])

def convert_to_schema(entry: CashFlowEntry) -> CashFlowEntrySchema:
    return CashFlowEntrySchema(
        entry_id=entry.get_entry_id(),
        amount=entry.get_amount(),
        entry_type=entry.get_type(),
        status=entry.get_status(),
        date=entry.get_date(),
    )

@router.get("/", response_model=List[CashFlowEntrySchema], tags=["Cash Flow"])
def fetch_all():
    entries = service.list_entries()
    return [convert_to_schema(e) for e in entries]

@router.post("/", response_model=CashFlowEntrySchema, tags=["Cash Flow"])
def create_entry(entry: CashFlowEntrySchema):
    try:
        entry_obj = CashFlowEntry(
            entry_id=entry.entry_id,
            amount=entry.amount,
            entry_type=entry.entry_type,
            status=entry.status,
            date=entry.date,
        )
        saved = service.add_entry(entry_obj)
        return convert_to_schema(saved)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{entry_id}", response_model=CashFlowEntrySchema, tags=["Cash Flow"])
def update_entry(entry_id: str, updated: CashFlowEntrySchema):
    updated_obj = CashFlowEntry(
        entry_id=updated.entry_id,
        amount=updated.amount,
        entry_type=updated.entry_type,
        status=updated.status,
        date=updated.date,
    )
    entry = service.update_entry(entry_id, updated_obj)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found.")
    return convert_to_schema(entry)

@router.patch("/{entry_id}", response_model=CashFlowEntrySchema, tags=["Cash Flow"])
def partial_update_entry(entry_id: str, updates: CashFlowEntryUpdateSchema):
    entry = service.get_entry(entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found.")

    # Update only provided fields
    if updates.amount is not None:
        entry._CashFlowEntry__amount = updates.amount
    if updates.entry_type is not None:
        entry._CashFlowEntry__type = updates.entry_type
    if updates.status is not None:
        entry._CashFlowEntry__status = updates.status
    if updates.date is not None:
        entry._CashFlowEntry__date = updates.date

    return convert_to_schema(entry)

@router.post("/{entry_id}/archive", response_model=CashFlowEntrySchema, tags=["Cash Flow"])
def archive_entry(entry_id: str):
    entry = service.archive_entry(entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found.")
    return convert_to_schema(entry)
