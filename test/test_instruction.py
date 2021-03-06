from models import (
    Recipe,
    Instruction,
    User,
    DataStore,
)

recipe_id   = 234234234234
user        = User('email@anonmail.com', 'weakpass')
instruction = Instruction(
    recipe_id,
    'New Instruction',
    118266162315588491253214850569623365886
)

ds = DataStore()

def test_create_instruction():
    """ It should create an instruction """
    title = 'Another one'
    description = 'Description for another one'

    instructions = ds.storage.get('instructions')
    if instructions is None:
        len_before = 0
    else:
        len_before = len(recipes)

    ds.create_instruction(
        recipe_id=recipe_id,
        title=title,
        description=description
    )
    len_after = ds.storage.get('instructions').__len__()
    assert len_after != 0
    assert len_before != len_after


def test_retrieve_instruction():
    ds.create_instruction(
        recipe_id=2934,
        title='Add a pinch of paprika',
        description='This makes the meal a little hot'
    )
    ds.create_instruction(
        recipe_id=2934,
        title='Add salt to water',
        description='The salt is for a bitter test and flavor'
    )

    # Retrieve random instruction from the database
    instruction_id = ds.storage.get('instructions')[0].get('id')
    assert instruction_id is not None
    searched_instruction = ds.find_instruction(instruction_id)
    assert searched_instruction is not None

    ds.storage.clear()  # Clean up data store


"""
def test_update_instruction():
    ds.create_instruction(
        recipe_id=2934,
        title='Add a pinch of paprika',
        description='This makes the meal a little hot'
    )
    ds.create_instruction(
        recipe_id=2934,
        title='Add salt to water',
        description='The salt is for a bitter test and flavor'
    )
    instruction_id = ds.storage.get('instructions')[0].get('id')
    print('Instruction ID is: {}'.format(instruction_id))
    assert recipe_id is not None

    ds.update_instruction(
        instruction_id=instruction_id,
        recipe_id=9471,
        title='Add a little salt to water',
        description='The salt is for a bitter test and flavor'
    )
    updated_instruction = ds.find_instruction(instruction_id)
    assert update_instruction.get('data').get('recipe_id') == 9471
    assert update_instruction.get('data').get('title') == 'Add a little salt to water'  # NOQA
"""


def test_delete_instruction():
    """ It should delete an instruction from the data store """
    title = 'Instruction for deletion'

    ds.create_instruction(recipe_id=recipe_id, title=title)
    len_before = ds.storage.get('instructions').__len__()
    instructions = ds.storage.get('instructions')
    instruction_id = ds.storage.get('instructions')[0].get('id')
    ds.delete_instruction(instruction_id)
    len_after = ds.storage.get('instructions').__len__()
    found = ds.find_instruction(instruction_id)
    assert found is None
    assert len_before != len_after
    assert len_before != 0


def test_recipe_instructions():
    """ It should return the instructions attached to a particular recipe """
    recipe_id   = 234234234234
    title       = 'Another one'
    description = 'Description for another one'

    recipe_id2   = 345345345345
    title2       = 'Add three spoonfuls of sugar'
    description2 = 'This gives the meal a sweet taste'

    recipe_id3   = 234234234234
    title3       = 'Sprinkle a little cayenne spice'
    description3 = 'This gives the meal some punch'

    Instruction.ds.create_instruction(
        recipe_id=recipe_id,
        title=title,
        description=description
    )
    Instruction.ds.create_instruction(
        recipe_id=recipe_id2,
        title=title2,
        description=description2
    )
    Instruction.ds.create_instruction(
        recipe_id=recipe_id3,
        title=title3,
        description=description3
    )
    instructions = Instruction.ds.recipe_instructions(recipe_id)
    assert instructions is not None
    assert instructions.__len__() == 2
    for instruction in instructions:
        assert instruction.get('data').get('recipe_id') == recipe_id
