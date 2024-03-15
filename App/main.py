from . import models
from .app import crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import schemas
from .database import SessionLocal, engine

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for films
@app.post("/films/", response_model=schemas.Film)
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db)):
    return crud.create_film(db=db, film=film)

@app.get("/films/{film_id}", response_model=schemas.Film)
def read_film(film_id: int, db: Session = Depends(get_db)):
    db_film = crud.get_film(db=db, film_id=film_id)
    if db_film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return db_film

@app.put("/films/{film_id}", response_model=schemas.Film)
def update_film(film_id: int, film: schemas.FilmUpdate, db: Session = Depends(get_db)):
    return crud.update_film(db=db, film_id=film_id, film=film)

@app.delete("/films/{film_id}")
def delete_film(film_id: int, db: Session = Depends(get_db)):
    return crud.delete_film(db=db, film_id=film_id)

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

# CRUD operations for companies
@app.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db=db, company=company)

@app.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.get_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@app.put("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    return crud.update_company(db=db, company_id=company_id, company=company)

@app.delete("/companies/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    return crud.delete_company(db=db, company_id=company_id)
