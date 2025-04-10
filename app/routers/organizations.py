from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/organizations", tags=["organizations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Organization])
def list_organizations(db: Session = Depends(get_db)):
    return crud.get_organizations(db)


@router.post("/", response_model=schemas.Organization)
def add_organization(organization: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    return crud.create_organization(db=db, organization=organization)


@router.delete("/{organization_id}")
def remove_organization(organization_id: int, db: Session = Depends(get_db)):
    return crud.delete_organization(db=db, organization_id=organization_id)
