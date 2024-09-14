from typing import Optional

from pydantic import BaseModel, Field
import datetime

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    created_at: int = Field(None, example='9月14日12:00')   # 追加
    stars: int = Field(None, example='3')   # 追加
    comment: Optional[str] = Field(None, example='すごい')  # 追加

class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    # done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True