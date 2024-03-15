# schemas.py

from pydantic import BaseModel
from typing import List

class FilmBase(BaseModel):
    title: str
    description: str
    budget: int
    release_year: int
    genres: List[str]

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    id: int

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    name: str
    contact_email_address: str
    phone_number: str

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True
