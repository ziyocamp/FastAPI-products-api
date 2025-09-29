from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import status, Path, Query

from app.db.database import LocalSession
from app.models.product import Product

router = APIRouter(
    prefix="/products",
    tags=["Product Endpoints"]
)


@router.get("")
def get_all_products(
    page: int = Query(1, ge=1), 
    limit: int = Query(10, ge=10, le=100)
):
    db = LocalSession()

    offset = (page - 1) * limit
    products = db.query(Product).offset(offset).limit(limit).all()

    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'price': product.price
        })

    return result


@router.get("/search")
def serach_products(
    search: str = Query(min_length=3, max_length=50),
):
    
    print(search)
    db = LocalSession()
    
    products = db.query(Product).filter(Product.name.ilike(f"%{search}%")).all()

    result = []
    for product in products:
        result.append({
            'id': product.id,
            'name': product.name,
            'price': product.price
        })

    return result


@router.get("/{product_id}")
def get_one_product(product_id: int = Path(gt=0)):
    db = LocalSession()
    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="bunday product mavjud emas.")

    return {
        'id': product.id,
        'name': product.name
    }


@router.put("/{product_id}")
def update_one_product(product_id: int):
    return {}
