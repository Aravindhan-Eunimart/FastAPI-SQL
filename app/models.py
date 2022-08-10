from sqlalchemy import ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, VARCHAR

from database import Base

class Student(Base):
    __tablename__ = "student"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(50), nullable=False)
    age = Column('age', Integer, nullable=False)
    class_ = Column('class', VARCHAR(50), nullable=False,)
    mother_name = Column('mother_name', VARCHAR(50), nullable=False)
    father_name = Column('father_name', VARCHAR(50), nullable=False)
    mother_occupation = Column('mother_occupation', VARCHAR(50), nullable=True)
    father_occupation = Column('father_occupation', VARCHAR(50), nullable=True)
    address = Column('address', String(150), nullable=False)
    phone_number_1 = Column('phone-number-1', String(10), nullable=False)
    phone_number_2 = Column('phone-number-2', String(10), nullable=True)
    email = Column('email', VARCHAR(50), nullable=True)

    class Config:
        orm_mode = True


class Progress(Base):
    __tablename__ = "progress"
    id = Column('id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey(
        "student.id", ondelete='CASCADE'), nullable=False)
    exam_name = Column('exam_name', VARCHAR(50), nullable=False)
    grade = Column('grade', VARCHAR(2))
    physics = Column('physics', Integer, nullable=False)
    chemistry = Column('chemistry', Integer, nullable=False)
    maths = Column('maths', Integer, nullable=False)
    total = Column('total', Integer, nullable=False)
    percentage = Column('percentage', Integer, nullable=False)
                 
