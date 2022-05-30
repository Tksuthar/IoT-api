from typing import Dict
from sqlalchemy.orm import Session
import models


def get_status(db: Session, id: int):
    return db.query(models.State).filter(models.State.id == id).first()

def create_defaut_state(db: Session):
    db_state = models.State(active=False)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state


def update_status(db: Session, id):
    data = db.query(models.State).filter(models.State.id == id).first()

    if data.active is True:
        data.active = False 
    else:
        data.active = True    
    db.commit()
    return db
