from pydantic import BaseModel
from typing import Optional


class OrganizationBase(BaseModel):
    name: str
    city: Optional[str] = None


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int

    class Config:
        orm_mode = True


class ContactBase(BaseModel):
    name: str
    phone: str
    city: Optional[str] = None
    organization_id: int


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    organization: Organization

    class Config:
        orm_mode = True
