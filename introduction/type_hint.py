# Dados de usuario

# name: string
# age: integer
# email: string

from pydantic import BaseModel, validator

# user = {
#     'name': 'carlos',
#     'age': 20,
#     'email': 'homelander@vougth.com'
# }


class User(BaseModel):
    name: str
    age: int
    email: str

    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email')
        return value


def f(user: User):
    pass


user = User(name='carlos', age=26, email='homelander@vougth.com')
print(user)
