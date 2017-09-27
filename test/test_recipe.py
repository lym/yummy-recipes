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
