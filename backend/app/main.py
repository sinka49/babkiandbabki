from fastapi import FastAPI, APIRouter
from datetime import datetime

from .routers.categoryRouter import category_router
from .routers.drinkRouter import drink_router
from .routers.ingridientRouter import ingridient_router

app = FastAPI()
main_api_router = APIRouter()
main_api_router.include_router(category_router, prefix="/categories", tags=["categories"])
main_api_router.include_router(ingridient_router, prefix="/ingridients", tags=["ingridients"])
main_api_router.include_router(drink_router, prefix="/drinks", tags=["drinks"])

app.include_router(main_api_router)