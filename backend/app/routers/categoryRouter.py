import uuid
from logging import getLogger

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..DAL.categoriesDal import Categories_Dal
from ..schemas.categories import categories_schema
from ..database import get_db

category_router = APIRouter()

logger = getLogger(__name__)


@category_router.get("/")
async def get_categories(db_session: AsyncSession = Depends(get_db)):
    posts = await _get_categories(db_session)
    if posts is None:
        raise HTTPException(
            status_code=404, detail=f"Posts not found."
        )
    return posts


async def _get_categories(db_session):
    async with db_session.begin():
        catsdal = Categories_Dal(db_session)
        cats = await catsdal.get_categories()
        if cats is not None:
            return cats


@category_router.get("/{ID}")
async def get_category(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        catsdal = Categories_Dal(db_session)
        category = await catsdal.get_category(ID=ID)
        if not category:
            raise HTTPException(status_code=404, detail=f'No post with this id: {ID} found')
        return category


@category_router.post("/", response_model=categories_schema)
async def create_category(body: categories_schema, db_session: AsyncSession = Depends(get_db), ) -> categories_schema:
    try:
        return await _create_new_categories(body, db_session)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


async def _create_new_categories(body: categories_schema, db_session):
    async with db_session.begin():
        catsdal = Categories_Dal(db_session)
        cat = await catsdal.create_categories(
            ID=body.ID,
            parrent_category=body.parrent_category,
            title=body.title,

        )

        return categories_schema(
            ID=cat.ID,
            parrent_category=cat.parrent_category,
            title=cat.title,

        )


@category_router.put("/{ID}")
async def update_category(updated_user_params: dict, ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        catsdal = Categories_Dal(db_session)
        updated_cat_id = await catsdal.update_category(ID=ID, **updated_user_params)
        return updated_cat_id


@category_router.delete("/{ID}", status_code=204)
async def delete_category(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        catsdal = Categories_Dal(db_session)
        await catsdal.delete_category(ID=ID)
