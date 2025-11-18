from pydantic import BaseModel


class Organization(BaseModel):
    name: str


class GetOrganization(BaseModel):
    name: str


class DeleteOrganization(BaseModel):
    name: str


class ListOrganizations(BaseModel):
    pass
