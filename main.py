# main.py

from fastapi import FastAPI
from api import cashflow
from api import inventory_item
from api import payment
from api import order

app = FastAPI(
    title="Informal Business Management",
    description="API for managing inventory, orders, payments, and cash flow in informal businesses.",
    version="1.0.0"
)

# Include API routers with tags
app.include_router(cashflow.router)
app.include_router(inventory_item.router)
app.include_router(payment.router)
app.include_router(order.router)



