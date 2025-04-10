from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/companies", tags=["companies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Company])
def list_companies(db: Session = Depends(get_db)):
    return crud.get_companies(db)

@router.post("/", response_model=schemas.Company)
def add_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db, company)

@router.delete("/{company_id}")
def remove_company(company_id: int, db: Session = Depends(get_db)):
    crud.delete_company(db, company_id)
    return {"message": "Deleted"}
