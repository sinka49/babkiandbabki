import uuid
from datetime import date
from sqlalchemy import select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..models.Base import Category, Drink, Drink_Ingridient, Ingridient


class Drinks_Dal:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_drinks(self, ID: uuid, title: str) -> Drink:
        drink = Drink(
            ID=ID,
            title=title
        )

        self.db_session.add(drink)
        await self.db_session.flush()
        return drink

    async def get_drinks(self) -> []:
        result = await self.db_session.execute(select(Drink).options(
            selectinload(Drink.ingridients).selectinload(Ingridient.values_for_ingridients)))
        drink_row = result.all()
        all_drinks = []
        for r in result:
            for i in r.ingridients:
                # i.selectinload(Ingridient.values_for_ingridients)
                print(i)
        print(result)
        for drink in drink_row:
            res = drink[0]
            all_drinks.append(res)
        return all_drinks

    async def get_drink(self, ID: uuid) -> Drink:
        result = await self.db_session.execute(select(Drink).where(Drink.ID == ID))
        drink_row = result.fetchone()
        if drink_row is not None:
            return drink_row[0]

    async def update_drink(self, ID: uuid, **kwargs):
        query = (
            update(Drink)
            .where(and_(Drink.ID == ID))
            .values(kwargs)
            .returning(Drink.ID)
        )
        res = await self.db_session.execute(query)
        update_drink_id_row = res.fetchone()
        if update_drink_id_row is not None:
            return update_drink_id_row[0]

    async def delete_drink(self, ID: uuid):
        query = delete(Drink).where(Drink.ID == ID)
        await self.db_session.execute(query)



