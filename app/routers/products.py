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
    min_price: float | None = Query(None, gt=0), 
    max_price: float | None = Query(None, gt=0)
):
    db = LocalSession()
    if min_price and max_price:
        products = db.query(Product).filter(Product.price >= min_price, Product.price <= max_price).all()
    elif min_price and max_price is None:
        products = db.query(Product).filter(Product.price >= min_price).all()
    elif min_price is None and max_price:
        products = db.query(Product).filter(Product.price <= max_price).all()
    else:
        products = db.query(Product).all()

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
