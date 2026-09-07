from pydantic import BaseModel


class MessageResponse(BaseModel):
    responseCode: int
    message: str


class User(BaseModel):
    id: int
    name: str
    email: str
    title: str
    birth_day: str
    birth_month: str
    birth_year: str
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str


class UserDetailsResponse(BaseModel):
    responseCode: int
    user: User
