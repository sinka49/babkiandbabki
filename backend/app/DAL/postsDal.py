import uuid
from datetime import date
from sqlalchemy import select, update, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.posts import Post


class posts_dal:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_posts(self, ID: uuid, user_id: uuid, title: str, content: str, created_at: date) -> Post:
        new_post = Post(
            ID=ID,
            user_id=user_id,
            title=title,
            content=content,
            created_at=created_at
        )

        self.db_session.add(new_post)
        await self.db_session.flush()
        return new_post

    async def get_posts(self) -> []:
        result = await self.db_session.execute(select(Post).order_by(Post.created_at))
        post_row = result.all()
        res = []
        for post in post_row:
            res.append(post[0])
        return res

    async def get_post(self, ID: uuid) -> Post:
        result = await self.db_session.execute(select(Post).where(Post.ID == ID))
        post_row = result.fetchone()
        if post_row is not None:
            return post_row[0]

    async def update_post(self, ID: uuid, **kwargs):
        query = (
            update(Post)
            .where(and_(Post.ID == ID))
            .values(kwargs)
            .returning(Post.ID)
        )
        res = await self.db_session.execute(query)
        update_post_id_row = res.fetchone()
        if update_post_id_row is not None:
            return update_post_id_row[0]

    async def delete_post(self, ID: uuid):
        query = delete(Post).where(Post.ID == ID)
        await self.db_session.execute(query)



