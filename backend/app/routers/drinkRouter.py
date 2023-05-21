import uuid
from logging import getLogger

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..DAL.drinksDal import Drinks_Dal
from ..schemas.drinks import drinks_schema
from ..database import get_db

drink_router = APIRouter()

logger = getLogger(__name__)


@drink_router.get("/")
async def get_drinks(db_session: AsyncSession = Depends(get_db)):
    drinks = await _get_drinks(db_session)
    if drinks is None:
        raise HTTPException(
            status_code=404, detail=f"drinks not found."
        )
    return drinks


async def _get_drinks(db_session):
    async with db_session.begin():
        drinksdal = Drinks_Dal(db_session)
        drinks = await drinksdal.get_drinks()
        if drinks is not None:
            return drinks


@drink_router.get("/{ID}")
async def get_drink(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        drinksdal = Drinks_Dal(db_session)
        drink = await drinksdal.get_drink(ID=ID)
        if not drink:
            raise HTTPException(status_code=404, detail=f'No drink with this id: {ID} found')
        return drink


@drink_router.post("/", response_model=drinks_schema)
async def create_category(body: drinks_schema, db_session: AsyncSession = Depends(get_db), ) -> drinks_schema:
    try:
        return await _create_new_drinks(body, db_session)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


async def _create_new_drinks(body: drinks_schema, db_session):
    async with db_session.begin():
        drinksdal = Drinks_Dal(db_session)
        drink = await drinksdal.create_drinks(
            ID=body.ID,
            title=body.title,
        )

        return drinks_schema(
            ID=drink.ID,
            title=drink.title,

        )


@drink_router.put("/{ID}")
async def update_drink(updated_user_params: dict, ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        drinksdal = Drinks_Dal(db_session)
        updated_drink_id = await drinksdal.update_drink(ID=ID, **updated_user_params)
        return updated_drink_id


@drink_router.delete("/{ID}", status_code=204)
async def delete_drink(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        drinksdal = Drinks_Dal(db_session)
        await drinksdal.delete_drink(ID=ID)
