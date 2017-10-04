from datetime import datetime
import pytz
import uuid
from tinydb import TinyDB  # , Query
from tinydb.storages import MemoryStorage


class DataStore:
    """ This is the DATA STRUCTURE THAT handles storage of all the models in
    the system.
    This is a dictionary (available to all models) that contains stored
    model records as lists of model objects accessible by `ids`
    """
    def __init__(self):
        self.tables = ('users', 'recipes', 'instructions', 'ingredients')
        self.user_attributes = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        )
        self.storage = {}.fromkeys(self.tables)
        # self.users_table = self.storage[

    def create_user(self, **user_data):
        _id = int(uuid.uuid4())
        user = {}

        for key, value in user_data.items():
            if key not in self.user_attributes:  # Accept only user attributes
                raise AttributeError('Please supply valid User attributes')
            user[key] = value
        if self.storage.get('users') is None:
            self.storage['users'] = [{'id': _id, 'data': user}]
            return self.storage.get('users')
        self.storage['users'].append({'id': _id, 'data': user})
        print(self.storage.get('users'))
        return self.storage.get('users')

    def find_user(self, user_id):
        """ DataStore.find_user(user_id) -> user instance or non """
        users = self.storage.get('users')
        if (users is None) or (len(users) == 0):
            return None
        for user in users:
            if user.get('id') == user_id:
                return user
            continue
        return None

    def update_user(self, user_id, **user_data):
        """ DataStore.update_user(): Update user records given the ID of the
        user
        """
        user = self.find_user(user_id)
        if user is None:  # User not in data store so no need to proceed
            raise ValueError()
        for key, value in user_data.items():
            if (key in user.get('data').keys()) or (key == 'user_id'):
                user.get('data')[key] = value
            else:  # Invalid user attributes
                raise Exception('Invalid User')

    def delete_user(self, user_id):
        user = self.find_user(user_id)
        if user is None:  # User not in data store so no need to proceed
            raise ValueError()
        users = self.storage.get('users')
        if (users is None) or (len(users) == 0):
            return None
        for user in users:
            if user.get('id') == user_id:
                self.storage['users'].remove(user)
        return None


    def valid_user(self, email, passw):
        # Return true if user with pass == user_pass is found in users table
        users = self.storage.get('users')
        if users is None:
            return
        for user in self.storage.get('users'):
            if ((user.get('data').get('email') == email) and
                    (user.get('data').get('password') == passw)):
                return True
            break
        return False


    def find_user_by_email(self, email):
        """ Lookup users by email """
        for user in self.storage.get('users'):
            if user.get('data').get('email') == email:
                return user
            return None



class BaseModel:
    """ This class implements all our models' shared features """
    table_name = None
    tz = pytz.utc

    db = TinyDB(storage=MemoryStorage)

    ds = DataStore()
    def __init__(self):
        self.id = id(self)  # guaranteed uniqueness through one program session
        self.created = datetime.now(self.tz)
        self.modified = datetime.now(self.tz)
