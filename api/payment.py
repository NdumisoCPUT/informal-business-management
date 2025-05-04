# api/payment.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from services.payment_service import PaymentService
from repositories.inmemory.payment_repository import InMemoryPaymentRepository
from src.payment import Payment

router = APIRouter(prefix="/api/payment", tags=["Payment"])

# Pydantic schema for request/response
class PaymentSchema(BaseModel):
    payment_id: str
    amount: float
    method: str
    status: str
    timestamp: datetime

# Create repository and service instances
repository = InMemoryPaymentRepository()
service = PaymentService(repository)

def to_schema(payment: Payment) -> PaymentSchema:
    return PaymentSchema(
        payment_id=payment.get_payment_id(),
        amount=payment.get_amount(),
        method=payment.get_method(),
        status=payment.get_status(),
        timestamp=payment.get_timestamp()
    )

@router.post("/", response_model=PaymentSchema)
def create_payment(payment: PaymentSchema):
    obj = Payment(
        payment_id=payment.payment_id,
        amount=payment.amount,
        method=payment.method,
        status=payment.status,
        timestamp=payment.timestamp
    )
    obj.process()
    return to_schema(service.add_payment(obj))

@router.get("/{payment_id}", response_model=PaymentSchema)
def get_payment(payment_id: str):
    payment = service.get_payment(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return to_schema(payment)

@router.get("/", response_model=list[PaymentSchema])
def list_payments():
    return [to_schema(p) for p in service.list_payments()]
