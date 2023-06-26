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
