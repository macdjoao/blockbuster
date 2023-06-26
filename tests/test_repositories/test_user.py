from faker import Faker

from src.infra.repositories.user import UserRepository

user_repository = UserRepository()
fake = Faker()


def test_insert():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(email=fake_email)

    # Checking equalities
    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_insert_EmailAlreadyRegisteredError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Second fake Payload
    second_fake_first_name = fake.first_name()
    second_fake_last_name = fake.last_name()

    # Trying insert second fake registry with same email of first fake registry
    fail_insert = user_repository.insert(
        email=fake_email,
        first_name=second_fake_first_name,
        last_name=second_fake_last_name,
        password=fake_password,
    )

    # Checking error
    assert fail_insert == f'Error: Email "{fake_email}" is already registered'

    # Selecting fake registry for delete
    query = user_repository.select(email=fake_email)

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_insert_ParamIsNotStringError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Setting a not string value
    fake_not_string = fake.random_digit()

    # Trying to insert by passing a not string value as email
    wrong_email_insert = user_repository.insert(
        email=fake_not_string,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Trying to insert by passing a not string value as first_name
    wrong_first_name_insert = user_repository.insert(
        email=fake_email,
        first_name=fake_not_string,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Trying to insert by passing a not string value as last_name
    wrong_last_name_insert = user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_not_string,
        password=fake_password,
    )

    # Trying to insert by passing a not string value as password
    wrong_password_insert = user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_not_string,
    )

    # Checking errors
    assert (
        wrong_email_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )
    assert (
        wrong_first_name_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )
    assert (
        wrong_last_name_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )
    assert (
        wrong_password_insert
        == f'Error: Param "{fake_not_string}" must be a string'
    )


def test_select():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()

    # Inserting fake
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Checking equalities
    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name
    assert query[0].is_active == True

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_select_ParamIsNotIntegerError():
    # Setting a not integer id
    fake_not_int_id = fake.word()

    # Trying to select a customer by passing a not integer as id
    query = user_repository.select(id=fake_not_int_id)

    # Checking error
    assert query == f'Error: Param "{fake_not_int_id}" must be a integer'


def test_select_ParamIsNotStringError():
    # Setting a not string email
    fake_not_string_email = fake.random_digit()
    # Trying to select a customer by passing a not string as email
    wrong_email_query = user_repository.select(email=fake_not_string_email)

    # Setting a not string first_name
    fake_not_string_first_name = fake.random_digit()
    # Trying to select a customer by passing a not string as first_name
    wrong_first_name_query = user_repository.select(
        first_name=fake_not_string_first_name
    )

    # Setting a not string last_name
    fake_not_string_last_name = fake.random_digit()
    # Trying to select a customer by passing a not string as last_name
    wrong_last_name_query = user_repository.select(
        last_name=fake_not_string_last_name
    )

    # Checking errors
    assert (
        wrong_email_query
        == f'Error: Param "{fake_not_string_email}" must be a string'
    )
    assert (
        wrong_first_name_query
        == f'Error: Param "{fake_not_string_first_name}" must be a string'
    )
    assert (
        wrong_last_name_query
        == f'Error: Param "{fake_not_string_last_name}" must be a string'
    )


def test_select_ParamIsNotBoolError():
    # Setting a not boolean is_active
    fake_not_bool_is_active = fake.word()
    # Trying to select a customer by passing a not boolean as is_active
    query = user_repository.select(is_active=fake_not_bool_is_active)

    # Checking errors
    assert (
        query == f'Error: Param "{fake_not_bool_is_active}" must be a boolean'
    )


def test_update():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()
    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Second fake payload
    new_fake_first_name = fake.first_name()
    new_fake_last_name = fake.last_name()
    # Update fake registry with second fake payload parameters
    user_repository.update(
        id=query[0].id,
        first_name=new_fake_first_name,
        last_name=new_fake_last_name,
    )

    # Selecting updated fake registry
    updated_query = user_repository.select(id=query[0].id)

    # Check equalities
    assert updated_query[0].first_name == new_fake_first_name
    assert updated_query[0].last_name == new_fake_last_name

    # Cleaning DB
    user_repository.delete(id=(updated_query[0].id))


def test_update_ParamIsNotIntegerError():
    # Fake wrong type id
    fake_wrong_id = fake.word()
    # Trying to update a registry by passing a not integer id
    update = user_repository.update(id=fake_wrong_id)

    # Checking error
    assert update == f'Error: Param "{fake_wrong_id}" must be a integer'


def test_update_ParamIsNotStringError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()
    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Not string value
    not_string_value = fake.random_digit()

    # Trying update fake registry with not string value
    wrong_email = user_repository.update(
        id=query[0].id, email=not_string_value
    )
    wrong_first_name = user_repository.update(
        id=query[0].id, first_name=not_string_value
    )
    wrong_last_name = user_repository.update(
        id=query[0].id, last_name=not_string_value
    )
    wrong_password = user_repository.update(
        id=query[0].id, password=not_string_value
    )

    # Checking errors
    assert wrong_email == f'Error: Param "{not_string_value}" must be a string'
    assert (
        wrong_first_name
        == f'Error: Param "{not_string_value}" must be a string'
    )
    assert (
        wrong_last_name
        == f'Error: Param "{not_string_value}" must be a string'
    )
    assert (
        wrong_password == f'Error: Param "{not_string_value}" must be a string'
    )

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_update_ParamIsNotBoolError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()
    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Setting a not boolean value
    not_boolean_value = fake.word()

    # Trying update fake registry with not string value
    wrong__is_active = user_repository.update(
        id=query[0].id, is_active=not_boolean_value
    )

    # Checking errors
    assert (
        wrong__is_active
        == f'Error: Param "{not_boolean_value}" must be a boolean'
    )

    # Cleaning DB
    user_repository.delete(id=(query[0].id))


def test_update_IdNotFoundError():
    # Fake payload
    fake_id = 0
    fake_last_name = fake.last_name()
    # Trying to update a registry passing an id that does not exist
    update = user_repository.update(id=fake_id, last_name=fake_last_name)

    # Checking error
    assert update == f'Error: Id "{fake_id}" not found'


def test_update_EmailAlreadyRegisteredError():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()
    # Inserting fake registry
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Second fake payload
    second_fake_email = fake.email()
    second_fake_first_name = fake.first_name()
    second_fake_last_name = fake.last_name()
    second_fake_password = fake.word()
    # Inserting second fake registry
    user_repository.insert(
        email=second_fake_email,
        first_name=second_fake_first_name,
        last_name=second_fake_last_name,
        password=second_fake_password,
    )

    # Selecting second fake registry
    second_query = user_repository.select(
        email=second_fake_email,
        first_name=second_fake_first_name,
        last_name=second_fake_last_name,
        is_active=True,
    )

    # Trying update second fake registry with a email that already exists (first payload's fake_email)
    already_exists_email = user_repository.update(
        id=second_query[0].id, email=fake_email
    )

    # Checking error
    assert (
        already_exists_email
        == f'Error: Email "{fake_email}" is already registered'
    )

    # Cleaning DB
    user_repository.delete(id=(query[0].id))
    user_repository.delete(id=(second_query[0].id))


def test_delete():
    # Fake payload
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_password = fake.word()
    # Inserting fake
    user_repository.insert(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        password=fake_password,
    )

    # Selecting fake registry
    query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Deleting fake registry
    user_repository.delete(id=(query[0].id))

    # Trying to select deleted fake registry
    delete_query = user_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    # Checking if registry is really deleted
    assert delete_query == []


def test_delete_ParamIsNotIntegerError():
    # Fake wrong type id
    fake_wrong_id = fake.word()
    # Trying to delete a registry by passing a not integer id
    delete = user_repository.delete(id=fake_wrong_id)

    # Checking error
    assert delete == f'Error: Param "{fake_wrong_id}" must be a integer'


def test_delete_IdNotFoundError():
    # Fake payload
    fake_id = 0
    # Trying to delete a registry passing an id that does not exist
    delete = user_repository.delete(id=fake_id)

    # Checking error
    assert delete == f'Error: Id "{fake_id}" not found'
