from sqlalchemy.orm import Session
from . import models, schemas

# Company CRUD
def get_companies(db: Session):
    return db.query(models.Company).all()

def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db_company = db.query(models.Company).get(company_id)
    if db_company:
        db.delete(db_company)
        db.commit()

# Contact CRUD
def get_contacts(db: Session):
    return db.query(models.Contact).all()

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).get(contact_id)
    if db_contact:
        db.delete(db_contact)
        db.commit()
