import uuid
from logging import getLogger

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..DAL.categoriesDal import Categories_Dal
from ..DAL.ingridientsDal import Ingridients_Dal
from ..database import get_db
from ..schemas.ingridients import ingridients_schema

ingridient_router = APIRouter()

logger = getLogger(__name__)


@ingridient_router.get("/")
async def get_ingridients(db_session: AsyncSession = Depends(get_db)):
    ings = await _get_ingridients(db_session)
    if ings is None:
        raise HTTPException(
            status_code=404, detail=f"Posts not found."
        )
    return ings


async def _get_ingridients(db_session):
    async with db_session.begin():
        ingsdal = Ingridients_Dal(db_session)
        ings = await ingsdal.get_ingridients()
        if ings is not None:
            return ings


@ingridient_router.get("/{ID}")
async def get_category(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        ingsdal = Ingridients_Dal(db_session)
        ing = await ingsdal.get_ingridient(ID=ID)
        if not ing:
            raise HTTPException(status_code=404, detail=f'No ingridient with this id: {ID} found')
        return ing


@ingridient_router.post("/", response_model=ingridients_schema)
async def create_ingridient(body: ingridients_schema, db_session: AsyncSession = Depends(get_db), ) -> ingridients_schema:
    try:
        return await _create_new_ingridients(body, db_session)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


async def _create_new_ingridients(body: ingridients_schema, db_session):
    async with db_session.begin():
        ingsdal = Ingridients_Dal(db_session)
        cat = await ingsdal.create_ingridients(
            ID=body.ID,
            title=body.title,

        )

        return ingridients_schema(
            ID=cat.ID,
            title=cat.title,
        )


@ingridient_router.put("/{ID}")
async def update_ingridient(updated_user_params: dict, ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        ingsdal = Ingridients_Dal(db_session)
        updated_ing_id = await ingsdal.update_ingridient(ID=ID, **updated_user_params)
        return updated_ing_id


@ingridient_router.delete("/{ID}", status_code=204)
async def delete_ingridient(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        ingsdal = Ingridients_Dal(db_session)
        await ingsdal.delete_ingridient(ID=ID)
