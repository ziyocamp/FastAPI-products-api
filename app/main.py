from fastapi import FastAPI

from app.routers.products import router as products_router
from app.routers.orders import router as orders_router

app = FastAPI()

app.include_router(products_router)
app.include_router(orders_router)
