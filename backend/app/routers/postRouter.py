import uuid
from logging import getLogger

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..DAL.postsDal import posts_dal

from ..schemas.posts import posts_schema
from ..database import get_db

post_router = APIRouter()

logger = getLogger(__name__)


@post_router.get("/")
async def get_posts(db_session: AsyncSession = Depends(get_db)):
    posts = await _get_posts(db_session)
    if posts is None:
        raise HTTPException(
            status_code=404, detail=f"Posts not found."
        )
    return posts


async def _get_posts(db_session):
    async with db_session.begin():
        postsdal = posts_dal(db_session)
        posts = await postsdal.get_posts()
        if posts is not None:
            return posts


@post_router.get("/{ID}")
async def get_post(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        postsdal = posts_dal(db_session)
        post = await postsdal.get_post(ID=ID)
        if not post:
            raise HTTPException(status_code=404, detail=f'No post with this id: {ID} found')
        return post


@post_router.post("/", response_model=posts_schema)
async def create_post(body: posts_schema, db_session: AsyncSession = Depends(get_db), ) -> posts_schema:
    try:
        return await _create_new_posts(body, db_session)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


async def _create_new_posts(body: posts_schema, db_session):
    async with db_session.begin():
        postsdal = posts_dal(db_session)
        post = await postsdal.create_posts(
            ID=body.ID,
            user_id=body.user_id,
            title=body.title,
            content=body.content,
            created_at=body.created_at
        )

        return posts_schema(
            ID=post.ID,
            user_id=post.user_id,
            title=post.title,
            content=post.content,
            created_at=post.created_at

        )


@post_router.put("/{ID}")
async def update_post(updated_user_params: dict, ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        postsdal = posts_dal(db_session)
        updated_post_id = await postsdal.update_post(ID=ID, **updated_user_params)
        return updated_post_id


@post_router.delete("/{ID}", status_code=204)
async def delete_post(ID: str, db_session: AsyncSession = Depends(get_db)):
    async with db_session.begin():
        postsdal = posts_dal(db_session)
        await postsdal.delete_post(ID=ID)
