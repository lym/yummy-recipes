from datetime import datetime
import uuid
from tinydb import where

from .base_model import BaseModel


class Recipe(BaseModel):
    table_name = 'recipes'

    def __init__(
        self, user_id, title, description='', fulfilled=False
    ):
        # super().__init__()
        self.title = title
        self.description = description
        self.fulfilled = fulfilled

    @classmethod
    def create(cls, **kwargs):
        db_table = cls.db.table(cls.table_name)
        if kwargs is None or len(kwargs) == 0:
            return
        if kwargs['user_id'] is None:
            return
        kwargs['created'] = datetime.now(cls.tz)
        kwargs['modified'] = datetime.now(cls.tz)
        for key, value in kwargs.items():
            kwargs[key] = value
        db_table.insert(
            {
                'id': int(uuid.uuid4()), 'data': kwargs
            }
        )

    @classmethod
    def delete(cls, _id):
        print('ID of Item for deletion'.format(_id))
        table = cls.db.table(cls.table_name)
        table.remove(where('id') == _id)

    @classmethod
    def all(cls):
        table = cls.db.table('recipes')
        return table.all()

    @classmethod
    def fetch(cls, recipe_id):
        table = Recipe.db.table(Recipe.table_name)
        results = table.get(where('id') == recipe_id)
        if len(results) > 0:
            return results
        return None
