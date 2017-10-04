from datetime import datetime
import uuid

from .base_model import BaseModel


class Recipe(BaseModel):

    def __init__(
        self, user_id, title, description='', fulfilled=False
    ):
        self.title = title
        self.description = description
        self.fulfilled = fulfilled
