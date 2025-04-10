from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/contacts", tags=["contacts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Contact])
def list_contacts(db: Session = Depends(get_db)):
    return crud.get_contacts(db)

@router.post("/", response_model=schemas.Contact)
def add_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)

@router.delete("/{contact_id}")
def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    crud.delete_contact(db, contact_id)
    return {"message": "Deleted"}
