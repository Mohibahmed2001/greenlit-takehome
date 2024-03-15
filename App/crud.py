from . import models
from sqlalchemy.orm import Session
from . import schemas

# CRUD operations for films
def create_film(db: Session, film: schemas.FilmCreate):
    db_film = models.Film(**film.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

def get_film(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.id == film_id).first()

def update_film(db: Session, film_id: int, film: schemas.FilmUpdate):
    db_film = db.query(models.Film).filter(models.Film.id == film_id).first()
    for key, value in film.dict().items():
        setattr(db_film, key, value)
    db.commit()
    db.refresh(db_film)
    return db_film

def delete_film(db: Session, film_id: int):
    db.query(models.Film).filter(models.Film.id == film_id).delete()
    db.commit()
    
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
    

# CRUD operations for companies
def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def update_company(db: Session, company_id: int, company: schemas.CompanyUpdate):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    for key, value in company.dict().items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db.query(models.Company).filter(models.Company.id == company_id).delete()
    db.commit()
