from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    # 追加(作成日時)、フロントからは編集できないようにする(defaultで値が入っている)
    created_at: datetime
    stars: int = Field(None, example='3')   # 追加
    comment: Optional[str] = Field(None, example='すごい')  # 追加
    updated_at: datetime

class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    #完了フラグ

    class Config:
        orm_mode = True