from tinydb import where

from app.models import (
    Recipe,
    Instruction,
    User
)

recipe = Recipe(883248, 'New Recipe')
user = User('email@anonmail.com', 'weakpass')
instruction = Instruction('New Instruction', 118266162315588491253214850569623365886)


def test_default_attributes():
    assert recipe.table_name is not None

    assert instruction.id is not None
    assert instruction.created is not None
    assert instruction.modified is not None

    assert user.id is not None
    assert user.created is not None
    assert user.modified is not None


def test_recipe_create():
    """ It should create an recipe """
    title = 'Another one'
    description = 'Description for another one'
    table = recipe.db.table('recipes')
    len_before = len(table.all())

    Recipe.create(title=title, description=description)
    len_after = len(table.all())
    assert len(recipe.db.table(recipe.table_name).all()) != 0
    assert len_before != len_after


def test_create_instruction():
    """It should create an instruction """
    title = 'New Instruction'
    recipe_id = instruction.recipe
    table = instruction.db.table('instructions')
    len_before = len(table.all())
    assert len_before == 0, 'No instructions yet'

    Instruction.create(title=title, recipe_id=recipe_id)
    len_after = len(table.all())
    assert len(table.all()) != 0, 'Expected at least one instruction in the instructions table'  # NOQA
    assert len_before != len_after
    assert len(instruction.db.table(instruction.table_name).all()) != 0
    assert len_before != len_after


def test_presence_of_table_names():
    """ Models should have table names """

    assert recipe.table_name is not None
    assert user.table_name is not None
    assert instruction.table_name is not None


def test_delete_instruction():
    title = 'Instruction for deletion'
    table = instruction.db.table('instructions')
    Instruction.create(title=title)
    len_before = len(table.all())
    assert len_before != 0

    rec_id = table.all()[-1].get('id')  # Get last-saved instruction
    Instruction.delete(rec_id)
    len_after = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_before != len_after
