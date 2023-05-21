import uuid
from datetime import date
from sqlalchemy import select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.Base import Category



class Categories_Dal:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_categories(self, ID: uuid, title: str, parrent_category: uuid) -> Category:
        category = Category(
            ID=ID,
            parrent_category=parrent_category,
            title=title
        )

        self.db_session.add(category)
        await self.db_session.flush()
        return category

    async def get_categories(self) -> []:
        result = await self.db_session.execute(select(Category))
        category_row = result.all()
        res = []
        for category in category_row:
            res.append(category[0])
        return res

    async def get_category(self, ID: uuid) -> Category:
        result = await self.db_session.execute(select(Category).where(Category.ID == ID))
        category_row = result.fetchone()
        if category_row is not None:
            return category_row[0]

    async def update_category(self, ID: uuid, **kwargs):
        query = (
            update(Category)
            .where(and_(Category.ID == ID))
            .values(kwargs)
            .returning(Category.ID)
        )
        res = await self.db_session.execute(query)
        update_category_id_row = res.fetchone()
        if update_category_id_row is not None:
            return update_category_id_row[0]

    async def delete_category(self, ID: uuid):
        query = delete(Category).where(Category.ID == ID)
        await self.db_session.execute(query)



