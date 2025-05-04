from fastapi import FastAPI
from api import cashflow
from api import inventory_item
from api import payment
from api import order





app = FastAPI(title="Informal Business Management",
    description="",
    version="1.0.0")
app.include_router(cashflow.router)
app.include_router(inventory_item.router)
app.include_router(payment.router)
app.include_router(order.router)


