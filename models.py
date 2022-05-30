from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.orm import relationship


from database import Base




class State(Base):

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    active = Column(Boolean, default=False)
