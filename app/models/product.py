from sqlalchemy import (
    Column, 
    Integer, 
    String,
    Text,
    Float,
    Boolean,
    DateTime
)

from app.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    description = Column(Text)
    category = Column(String(length=50))
    brand = Column(String(length=50))
    price = Column(Float)
    currency = Column(String(50))
    quantity_in_stock = Column(Integer)
    is_active = Column(Boolean)
    discount_percent = Column(Integer)
    rating = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
