from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        print("Object created!")
        # return db
        yield db
    finally:
        print("DB object closed!")
        db.close()


@app.get("/status/{id}")
def read_user(id: int, db: Session = Depends(get_db)):
    status = crud.get_status(db, id=id)

    if status is None:
        crud.create_defaut_state(db)
        return crud.get_status(db, id=id)
    
    return status

@app.put('/update')
def update_status(db: Session = Depends(get_db)):
    result = crud.update_status(db, id=1)
    return result

