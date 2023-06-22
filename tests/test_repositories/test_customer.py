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
