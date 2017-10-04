from models import (
    User,
    Recipe,
    DataStore,
)

recipe = Recipe(883248, 'New Recipe')
user = User('email@anonmail.com', 'weakpass')
ds = DataStore()


def test_recipe_create():
    """ It should create an recipe """
    user_id = 12345
    title = 'Another one'
    description = 'Description for another one'

    recipes = ds.storage.get('recipes')
    if recipes is None:
        len_before = 0
    else:
        len_before = len(recipes)

    ds.create_recipe(user_id=user_id, title=title, description=description)
    len_after = ds.storage.get('recipes').__len__()
    assert len_after != 0
    assert len_before != len_after

    ds.storage.clear()  # Clean up data store


def test_retrieve_recipe():
    ds.create_recipe(
        user_id='123',
        title='New Recipe',
        description='A desc for the new recipe'
    )

    ds.create_recipe(
        user_id='123',
        title='Another Recipe',
        description='A desc for the another recipe'
    )

    # Retrieve random recipe from the database
    recipe_id = ds.storage.get('recipes')[0].get('id')
    assert recipe_id is not None
    searched_recipe = ds.find_recipe(recipe_id)
    assert searched_recipe is not None

    ds.storage.clear()  # Clean up data store


def test_update_recipe():
    ds.create_recipe(
        user_id=123,
        title='New Recipe',
        description='A desc for the new recipe'
    )

    ds.create_recipe(
        user_id=123,
        title='Another Recipe',
        description='A desc for the another recipe'
    )

    recipe_id = ds.storage.get('recipes')[0].get('id')
    assert recipe_id is not None

    ds.update_recipe(
        recipe_id,
        user_id=324,
        title='New Recipe',
        description='A desc for t'
    )
    updated_recipe = ds.find_recipe(recipe_id)
    assert updated_recipe.get('data').get('description') == 'A desc for t'
    assert updated_recipe.get('data').get('user_id') == 324


def test_delete_recipe():
    """ It should delete a recipe instance from the recipes table """
    user_id = 12345
    title = 'Item for deletion'

    ds.create_recipe(
        user_id=user_id,
        title=title,
        description='This item is meant to test the delete functionality'
    )
    len_before = ds.storage.get('recipes').__len__()
    recipes = ds.storage.get('recipes')
    recipe_id = ds.storage.get('recipes')[0].get('id')
    ds.delete_recipe(recipe_id)
    len_after = ds.storage.get('recipes').__len__()
    found = ds.find_recipe(recipe_id)
    assert found is None
    assert len_before != len_after
    assert len_before != 0
