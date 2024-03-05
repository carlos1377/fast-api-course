from pydantic import BaseModel, Field, validator
import re
"""
{
    "price": 12312,
    "to_currencies": ['USD','EUR','GBP'],
}
"""


class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: list[str]

    @validator('to_currencies')
    def validate_to_currencies(cls, value):
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Invalid Currency {currency}')
        return value


class ConverterOutput(BaseModel):
    message: str
    data: list[dict]
