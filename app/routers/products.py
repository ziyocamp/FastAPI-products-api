from typing import Literal

from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status, Path, Query
from sqlalchemy import desc

from app.db.database import LocalSession
from app.models.product import Product
from app.schemas.products import ProductResponse, ProductListResponse, ProductSearchListResponse

router = APIRouter(
    prefix="/products",
    tags=["Product Endpoints"]
)


@router.get("", response_model=ProductListResponse)
def get_all_products(
    page: int = Query(1, ge=1), 
    limit: int = Query(10, ge=10, le=100),
    order_by: Literal['created_at', 'updated_at'] = 'updated_at',
    order_sort: Literal['asc', 'desc'] = 'asc'
):
    db = LocalSession()

    offset = (page - 1) * limit
    if order_by == "updated_at":
        if order_sort == "desc":
            products = db.query(Product).order_by(desc(Product.updated_at)).offset(offset).limit(limit).all()
        else:
            products = db.query(Product).order_by(Product.updated_at).offset(offset).limit(limit).all()
    else:
        if order_sort == "desc":
            products = db.query(Product).order_by(desc(Product.created_at)).offset(offset).limit(limit).all()
        else:
            products = db.query(Product).order_by(Product.created_at).offset(offset).limit(limit).all()

    total = db.query(Product).count()

    pages = total // limit + (1 if total % limit != 0 else 0)

    return ProductListResponse(products=products, total=total, limit=limit, pages=pages, page=page)


@router.get("/search", response_model=ProductSearchListResponse)
def serach_products(
    search: str = Query(min_length=3, max_length=50),
):
    db = LocalSession()
    
    products = db.query(Product).filter(Product.name.ilike(f"%{search}%")).all()

    return ProductSearchListResponse(products=products)



@router.get("/orderby", response_model=ProductSearchListResponse)
def order_products():
    db = LocalSession()
    
    products = db.query(Product).order_by(Product.updated_at).all()

    return ProductSearchListResponse(products=products)

@router.get("/{product_id}", response_model=ProductResponse)
def get_one_product(product_id: int = Path(gt=0)):
    db = LocalSession()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="bunday product mavjud emas.")

    return product


@router.put("/{product_id}")
def update_one_product(product_id: int):
    return {}
