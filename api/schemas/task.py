from typing import Optional

from pydantic import BaseModel, Field
import datetime

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    # 追加(作成日時)、フロントからは編集できないようにする(defaultで値が入っている)
    created_at: str = Field(None, example=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S"))
    stars: int = Field(None, example='3')   # 追加
    comment: Optional[str] = Field(None, example='すごい')  # 追加
    updated_at: str = Field(None, example=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S"))

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