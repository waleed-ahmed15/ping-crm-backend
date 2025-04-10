from pydantic import BaseModel
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    city: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    name: str
    phone: str
    city: Optional[str] = None
    company_id: int

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    company: Company
    class Config:
        orm_mode = True
