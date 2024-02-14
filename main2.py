# from enum import Enum
# from fastapi import FastAPI
# from pydantic import BaseModel


# class Nome(str, Enum):
#     carlos = 'carlos'
#     eduardo = 'eduardo'
#     orso = 'orso'


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.post('/items/')
# async def create_item(item: Item):
#     return item


# @app.get('/user/me')
# async def get_user():
#     return {'user_id': 'current user'}


# @app.get('/user/{user_id}')
# async def read_item(user_id: int):
#     return {'user_id': user_id}


# @app.get('/models/{name}')
# async def get_model(name: Nome):
#     if name is Nome.carlos:
#         return {'nome': name, 'message': 'oi carlinhos'}
#     if name is Nome.eduardo:
#         return {'nome': name, 'message': 'oi duds'}
#     return {'nome': name, 'message': 'oi urso'}


# @app.get('/file/{file_path:path}')
# async def read_file(file_path: str):
#     return {'file_path': file_path}

# fake_items_db = [{"item_name": "Foo"}, {
#     "item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get('/items/')
# async def get_item(skip: int = 0, limit: int = 3):
#     return fake_items_db[skip:skip+limit]
