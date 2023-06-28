from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str


class CreatedUser(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool


class ReadUsers(BaseModel):
    id: int
