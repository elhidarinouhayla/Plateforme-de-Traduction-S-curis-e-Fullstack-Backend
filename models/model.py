from sqlalchemy import Column, String, Float, Integer 
from database import Base
from pydantic import BaseModel


print(Base)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class CreateUser(BaseModel):
    username : str
    password : str


class ResponseUser(CreateUser):
    id : int


class TraductionShema(BaseModel):
    text : str
    language : str