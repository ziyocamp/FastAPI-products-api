from fastapi.routing import APIRouter

router = APIRouter(
    tags=['Orders Endpoints']
)


@router.get("/orders")
def get_all_orders():
    return {}


@router.get("/orders/{order_id}")
def get_one_order(order_id: int):
    return {}

