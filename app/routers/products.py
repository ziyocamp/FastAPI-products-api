from fastapi.routing import APIRouter

router = APIRouter(
    tags=["Product Endpoints"]
)


@router.get("/products")
def get_all_products():
    return {}


@router.get("/products/{product_id}")
def get_one_product(product_id: int):
    return {}

