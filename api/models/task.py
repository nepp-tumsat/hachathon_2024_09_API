from sqlalchemy import Column, Integer, String, ForeignKey, Time, CheckConstraint
from sqlalchemy.orm import relationship

from api.db import Base
import datetime        # 追加(import)

class Task(Base):
    __tablename__ = "books_review"     # 変更(tasks→books_review)

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    # 追加(作成日時)、フロントからは編集できないようにする(defaultで値が入っている)
    created_at = Column(String(50),nullable=False)
    stars = Column(Integer, CheckConstraint('stars >=0 AND stars <=5'), nullable=False)  # 追加(星の数)
    comment = Column(String(200))   # 追加(本へのコメント)
    updated_at = Column(String(50),nullable=False)  # 追加(更新日時)

    done = relationship("Done", back_populates="task", cascade="delete")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("books_review.id"), primary_key=True)

    task = relationship("Task", back_populates="done")