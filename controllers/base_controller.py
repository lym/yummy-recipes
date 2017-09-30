from flask import session

class BaseController:
    @classmethod
    def logged_in(cls):
        if session.get('user') is None:
            return False
        return True

