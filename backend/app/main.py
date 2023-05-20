from fastapi import FastAPI, APIRouter
from datetime import datetime

from .routers.categoryRouter import category_router

app = FastAPI()
main_api_router = APIRouter()
main_api_router.include_router(category_router, prefix="/categories", tags=["categories"])

app.include_router(main_api_router)