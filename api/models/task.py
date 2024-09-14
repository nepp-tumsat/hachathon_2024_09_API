from sqlalchemy import Column, Integer, String, ForeignKey, Time, CheckConstraint
from sqlalchemy.orm import relationship

from api.db import Base
import datetime        # 追加(import)

class Task(Base):
    __tablename__ = "tasks"     # 変更(tasks→books_review)

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    created_at = Column(Time,nullable=False, default=datetime.datetime.now)   # 追加(作成日時)
    stars = Column(Integer, CheckConstraint('stars >=0 AND stars <=5'), nullable=False)  # 追加(星の数)
    comment = Column(String(200))   # 追加(本へのコメント)

    done = relationship("Done", back_populates="task", cascade="delete")  


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="done")