from tinydb import where

from models import (
    Recipe,
    Instruction,
    User
)

recipe_id   = 234234234234
user        = User('email@anonmail.com', 'weakpass')
instruction = Instruction(
    recipe_id,
    'New Instruction',
    118266162315588491253214850569623365886
)


def test_default_attributes():
    assert instruction.table_name is not None
    assert instruction.created is not None
    assert instruction.modified is not None


def test_create_instruction():
    """ It should create an instruction """
    title = 'Another one'
    description = 'Description for another one'
    table = instruction.db.table('instructions')
    len_before = len(table.all())

    Instruction.create(recipe_id=recipe_id, title=title, description=description)
    len_after = len(table.all())
    assert len(table.all()) != 0, 'Expected at least one instruction in the instructions table'  # NOQA
    assert len_before != len_after


def test_presence_of_table_names():
    """ Models should have table names """

    assert instruction.table_name is not None
    assert user.table_name is not None
    assert instruction.table_name is not None


def test_delete_instruction():
    title = 'Instruction for deletion'
    table = instruction.db.table('instructions')
    len_before = len(table.all())
    Instruction.create(recipe_id=recipe_id, title=title)
    len_after_insert = len(table.all())
    assert len_before != len_after_insert

    rec_id = table.all()[-1].get('id')  # Get last-saved instruction
    Instruction.delete(rec_id)
    len_after_deletion = len(table.all())
    found = table.get(where('id') == rec_id)
    assert found is None
    assert len_after_insert != len_after_deletion
