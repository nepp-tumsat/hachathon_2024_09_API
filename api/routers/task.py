from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()


@router.get("/get_reviews", response_model=List[task_schema.Task])
async def list_reviews(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)


@router.post("/post_reviews", response_model=task_schema.TaskCreateResponse)
async def post_reviews(
    task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.post_reviews(db, task_body)


@router.put("/put_reviews/{reviews_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    reviews_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, reviews_id=reviews_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_body, original=task)


@router.delete("/delete_reviews/{reviews_id}", response_model=None)
async def delete_task(reviews_id: int):
    return
