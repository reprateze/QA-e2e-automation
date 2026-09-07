from pydantic import BaseModel


class Brand(BaseModel):
    id: int
    brand: str


class BrandsListResponse(BaseModel):
    responseCode: int
    brands: list[Brand]
