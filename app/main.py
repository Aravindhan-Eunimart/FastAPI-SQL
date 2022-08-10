import uvicorn
from fastapi import FastAPI, Depends, status
from database import get_db
from schemas import ProgressBase, StudentBase, StudentPublic, StudentWithProgress
from sqlalchemy.orm import Session


import service


app = FastAPI()

DEBUG = True


@app.get("/student/{id}")
async def get_single(id: int, db: Session = Depends(get_db)):
    status = service.get_single_record(id, db)
    return status 


@app.get('/student/')
def get_all(db: Session = Depends(get_db)):
    status = service.get_all_record(db)
    return status


@app.post('/student/', status_code=status.HTTP_201_CREATED)
async def insert_single(student: StudentBase, progress: ProgressBase, db: Session = Depends(get_db)):
    print(student)
    print(progress)
    status = service.insert_single_record(student, progress, db)
    return status


@app.post('/students/', status_code=status.HTTP_201_CREATED)
async def insert_many(students: list[StudentWithProgress], db: Session = Depends(get_db)):
    # print(students)
    status = service.insert_multiple_record(students, db)
    return status


@app.delete('/student/{id}')
def delete_single(id: int, db: Session = Depends(get_db)):
    status = service.delete_single_record(id, db)
    return status


@app.delete('/student/')
def delete_all(db: Session = Depends(get_db)):
    status = service.delete_all_record(db)
    return status


if __name__ == "__main__":
    uvicorn.run("main:app", debug=DEBUG, port=5000, reload=True)
