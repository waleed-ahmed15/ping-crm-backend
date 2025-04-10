from sqlalchemy.orm import Session
from . import models, schemas

# Organization CRUD


def get_organizations(db: Session):
    return db.query(models.Organization).all()


def create_organization(db: Session, organization: schemas.OrganizationCreate):
    db_organization = models.Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def delete_organization(db: Session, organization_id: int):
    db_organization = db.query(models.Organization).get(organization_id)
    if db_organization:
        db.delete(db_organization)
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
