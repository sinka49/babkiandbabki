import uuid
from datetime import date
from sqlalchemy import select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.Base import Ingridient


class Ingridients_Dal:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_ingridients(self, ID: uuid, title: str, ) -> Ingridient:
        ingridient = Ingridient(
            ID=ID,
            title=title
        )

        self.db_session.add(ingridient)
        await self.db_session.flush()
        return ingridient

    async def get_ingridients(self) -> []:
        result = await self.db_session.execute(select(Ingridient))
        ingridient_row = result.all()
        res = []
        for ingridient in ingridient_row:
            res.append(ingridient[0])
        return res

    async def get_ingridient(self, ID: uuid) -> Ingridient:
        result = await self.db_session.execute(select(Ingridient).where(Ingridient.ID == ID))
        ingridient_row = result.fetchone()
        if ingridient_row is not None:
            return ingridient_row[0]

    async def update_ingridient(self, ID: uuid, **kwargs):
        query = (
            update(Ingridient)
            .where(and_(Ingridient.ID == ID))
            .values(kwargs)
            .returning(Ingridient.ID)
        )
        res = await self.db_session.execute(query)
        update_category_id_row = res.fetchone()
        if update_category_id_row is not None:
            return update_category_id_row[0]

    async def delete_ingridient(self, ID: uuid):
        query = delete(Ingridient).where(Ingridient.ID == ID)
        await self.db_session.execute(query)
