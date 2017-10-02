from datetime import datetime
import uuid
from tinydb import where
from .base_model import BaseModel


class Instruction(BaseModel):
    table_name = 'instructions'

    def __init__(self, recipe_id, title, description=''):
        super().__init__()
        self.recipe_id = recipe_id
        self.title = title
        self.description = description

    @classmethod
    def create(cls, **kwargs):
        print('Arguments dictionary: {}'.format(kwargs))
        db_table = cls.db.table(cls.table_name)
        if (kwargs is None) or (kwargs.get('recipe_id') is None):
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
        table = cls.db.table('instructions')
        return table.all()

    @classmethod
    def find(cls, instruction_id):
        """ Look up instructions by ID """
        for instruction in cls.all():
            if instruction.get('id') == instruction_id:
                return instruction
            return None
