from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    category: str
    brand:str 
    price: float
    currency: str
    quantity_in_stock: int
    is_active: bool
    discount_percent: int | None = None
    rating: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int
    limit: int
    pages: int
    page: int

    class Config:
        from_attributes = True


class ProductSearchListResponse(BaseModel):
    products: List[ProductResponse]

    class Config:
        from_attributes = True

