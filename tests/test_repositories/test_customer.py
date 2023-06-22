from faker import Faker

from src.infra.repositories.customer import CustomerRepository

customer_repository = CustomerRepository()
fake = Faker()


def test_insert():
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()

    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    query = customer_repository.select(email=fake_email)

    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name


def test_insert_EmailAlreadyRegisteredError():
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    second_fake_first_name = fake.first_name()
    second_fake_last_name = fake.last_name()
    fail_insert = customer_repository.insert(
        email=fake_email,
        first_name=second_fake_first_name,
        last_name=second_fake_last_name,
    )

    assert fail_insert == f'Error: Email "{fake_email}" is already registered'


def test_select():
    fake_email = fake.email()
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    customer_repository.insert(
        email=fake_email, first_name=fake_first_name, last_name=fake_last_name
    )

    query = customer_repository.select(
        email=fake_email,
        first_name=fake_first_name,
        last_name=fake_last_name,
        is_active=True,
    )

    assert query[0].email == fake_email
    assert query[0].first_name == fake_first_name
    assert query[0].last_name == fake_last_name
    assert query[0].is_active == True


def test_select_ParamIsNotIntegerError():

    fake_not_int_id = fake.word()
    query = customer_repository.select(id=fake_not_int_id)

    assert query == f'Error: Param "{fake_not_int_id}" must be a integer'


def test_select_ParamIsNotStringError():

    fake_not_string_email = fake.random_digit()
    wrong_email_query = customer_repository.select(email=fake_not_string_email)

    fake_not_string_first_name = fake.random_digit()
    wrong_first_name_query = customer_repository.select(
        email=fake_not_string_first_name
    )

    fake_not_string_last_name = fake.random_digit()
    wrong_last_name_query = customer_repository.select(
        email=fake_not_string_last_name
    )

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

    fake_not_bool_is_active = fake.word()
    query = customer_repository.select(is_active=fake_not_bool_is_active)

    assert query == f'Error: Param {fake_not_bool_is_active} must be a boolean'
