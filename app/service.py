from sqlalchemy.orm import Session
from models import Progress, Student
from schemas import ProgressBase, StudentBase, StudentWithProgress
from fastapi import HTTPException


def get_single_record(id: int, db: Session):
    result = db.query(Student).filter(Student.id == id).first()
    if result == None:
        raise HTTPException(status_code=404, detail={"message": "Record doesn't exist!"})
    # breakpoint()
    return result


def get_all_record(db: Session):
    result = db.query(Student).all()
    return result


def delete_single_record(id: int, db: Session):
    result = db.query(Student).filter_by(id=id).delete()
    if result == 0:
        raise HTTPException(status_code=404, detail={"message": "Record doesn't exist!"})
    db.commit()


def delete_all_record(db: Session):
    result = db.query(Student).delete()
    db.commit()


def insert_single_record(stud_data: StudentBase, prog_data: ProgressBase, db: Session):
    student = Student(**stud_data.dict())
    progress = Progress(**prog_data.dict())
    db.add(student)
    db.commit()
    progress.student_id = student.id
    db.add(progress)
    db.commit()


def insert_multiple_record(stud_datas: list[StudentWithProgress], db: Session):
    for data in stud_datas:
        stud_data = data.student
        prog_data = data.progress
        student = Student(**stud_data.dict())
        progress = Progress(**prog_data.dict())
        db.add(student)
        db.commit()
        progress.student_id = student.id
        db.add(progress)
        db.commit()