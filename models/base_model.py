from datetime import datetime
import pytz
import uuid


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
        self.recipe_attributes = (
            'user_id',
            'title',
            'description',
            'fulfilled'
        )
        self.instruction_attributes = (
            'recipe_id',
            'title',
            'description'
        )
        self.storage = {}.fromkeys(self.tables)

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

    """ Recipes Section """
    def create_recipe(self, **recipe_data):
        _id = int(uuid.uuid4())
        recipe = {}

        for key, value in recipe_data.items():
            if key not in self.recipe_attributes:  # Accept only Recipe attributes  # NOQA
                raise AttributeError('Please supply valid Recipe attributes')
            recipe[key] = value
        if self.storage.get('recipes') is None:
            self.storage['recipes'] = [{'id': _id, 'data': recipe}]
            return self.storage.get('recipes')
        self.storage['recipes'].append({'id': _id, 'data': recipe})
        print(self.storage.get('recipes'))
        return self.storage.get('recipes')

    def find_recipe(self, recipe_id):
        """ DataStore.find_recipe(recipe_id) -> recipe instance or none """
        recipes = self.storage.get('recipes')
        if (recipes is None) or (len(recipes) == 0):
            return None
        for recipe in recipes:
            if recipe.get('id') == recipe_id:
                return recipe
            continue
        return None

    def update_recipe(self, recipe_id, **recipe_data):
        """ DataStore.update_recipe(): Update recipe records given the ID of the
        recipe
        """
        recipe = self.find_recipe(recipe_id)
        if recipe is None:  # Recipe not in data store so no need to proceed
            raise ValueError()
        for key, value in recipe_data.items():
            if (key in recipe.get('data').keys()) or (key == 'recipe_id'):
                recipe.get('data')[key] = value
            else:  # Invalid recipe attributes
                raise Exception('Invalid Recipe')

    def delete_recipe(self, recipe_id):
        recipe = self.find_recipe(recipe_id)
        if recipe is None:  # Recipe not in data store so no need to proceed
            raise ValueError()
        recipes = self.storage.get('recipes')
        if (recipes is None) or (len(recipes) == 0):
            return None
        for recipe in recipes:
            if recipe.get('id') == recipe_id:
                self.storage['recipes'].remove(recipe)
        return None


    """ Instructions section """
    def create_instruction(self, **instruction_data):
        _id = int(uuid.uuid4())
        instruction = {}

        for key, value in instruction_data.items():
            if key not in self.instruction_attributes:  # Accept only Recipe attributes  # NOQA
                raise AttributeError('Please supply valid Instruction attributes')  # NOQA
            instruction[key] = value
        if self.storage.get('instructions') is None:
            self.storage['instructions'] = [{'id': _id, 'data': instruction}]
            return self.storage.get('instructions')
        self.storage['instructions'].append({'id': _id, 'data': instruction})
        return self.storage.get('instructions')

    def find_instruction(self, instruction_id):
        """ DataStore.find_instruction(instruction) -> instruction instance or none """
        instructions = self.storage.get('instructions')
        if (instructions is None) or (len(instructions) == 0):
            return None
        for instruction in instructions:
            if instruction.get('id') == instruction_id:
                return instruction
            continue
        return None

    def update_instruction(self, instruction_id, **instruction_data):
        """ DataStore.update_instruction(): Update Instruction records given
        the ID of the instruction
        """
        instruction = self.find_instruction(instruction_id)
        if instruction is None:  # Instruction not in data store so no need to proceed
            raise ValueError()
        for key, value in instruction.items():
            if (key in instruction.get('data').keys()) or (key == 'instruction_id'):
                instruction.get('data')[key] = value
            else:  # Invalid instruction attributes
                raise Exception('Invalid Instruction')

    def delete_instruction(self, instruction_id):
        instruction = self.find_instruction(instruction_id)
        if instruction is None:  # Instruction not in data store so no need to proceed
            raise ValueError()
        instructions = self.storage.get('instructions')
        if (instructions is None) or (len(instructions) == 0):
            return None
        for instruction in instructions:
            if instruction.get('id') == instruction_id:
                self.storage['instructions'].remove(instruction)
        return None



class BaseModel:
    """ This class implements all our models' shared features """
    tz = pytz.utc
    ds = DataStore()

    def __init__(self):
        self.id = id(self)  # guaranteed uniqueness through one program session
        self.created = datetime.now(self.tz)
        self.modified = datetime.now(self.tz)
