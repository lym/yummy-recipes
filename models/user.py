from datetime import datetime
import hashlib
from .base_model import BaseModel


class User(BaseModel):
    def __init__(
        self, email, password, first_name='', last_name='', username=''
    ):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self._enc_passw(password)

    def _enc_passw(self, pw):
        safe_passw = pw.encode()
        msg = hashlib.sha256()
        msg.update(safe_passw)
        return msg
