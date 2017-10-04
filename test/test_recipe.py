from tinydb import where

from models import (
    User,
    Recipe
)

recipe = Recipe(883248, 'New Recipe')
user = User('email@anonmail.com', 'weakpass')


def test_default_attributes():
    assert recipe.table_name is not None


def test_recipe_create():
    """ It should create an recipe """
    user_id = 12345
    title = 'Another one'
    description = 'Description for another one'
    table = recipe.db.table('recipes')
    len_before = len(table.all())

    Recipe.create(user_id=user_id, title=title, description=description)
    len_after = len(table.all())
    assert len(recipe.db.table(recipe.table_name).all()) != 0
    assert len_before != len_after

    Recipe.db.purge_tables()  # Clean up data store


def test_presence_of_table_name_attribute():
    """ Models should have table names """
    assert recipe.table_name is not None


def test_delete_recipe():
    """ It should delete a recipe instance from the recipes table """
    user_id = 12345
    title = 'Item for deletion'
    table = recipe.db.table(recipe.table_name)
    Recipe.create(
        user_id=user_id,
        title=title,
        description='This item is meant to test the delete functionality'
    )
    len_before = len(table.all())
    assert len_before != 0

    rec_id = table.all()[-1].get('id')
    Recipe.delete(rec_id)
    len_after = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_before != len_after

    Recipe.db.purge_tables()  # Clean up data store

def test_recipes_fetch():
    """ It should return recipes given a recipe id """
    user_id = 12345  # owner of recipes
    title_1 = 'First Recipe'
    title_2 = 'Second Recipe'
    title_3 = 'Third Recipe'
    description_1 = 'This is a description for First Recipe'
    description_2 = 'This is a description for Second Recipe'
    description_3 = 'This is a description for Third Recipe'

    Recipe.create(
        user_id=user_id,
        title=title_1,
        description=description_1
    )

    Recipe.create(
        user_id=user_id,
        title=title_2,
        description=description_2
    )

    Recipe.create(
        user_id=user_id,
        title=title_3,
        description=description_3
    )

    recipes = Recipe.all()
    recipe_ids = []
    for recipe in recipes:
        recipe_ids.append(recipe.get('id'))
    print('Number or recipes: {}'.format(len(recipe_ids)))
    print('The three test recipes: {}'.format(recipe_ids))
    recipe_id = recipe_ids.pop()
    fetched_recipe = Recipe.fetch(recipe_id)
    print('Fetched Recipe: {}'.format(fetched_recipe))
    assert fetched_recipe is not None
    # assert Recipe.fetch(recipe_id)
    Recipe.db.purge_tables()  # Clean up data store
