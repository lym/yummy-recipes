from datetime import datetime
import uuid
from .base_model import BaseModel


class Instruction(BaseModel):
    def __init__(self, recipe_id, title, description=''):
        super().__init__()
        self.recipe_id = recipe_id
        self.title = title
        self.description = description
