from faker import Faker

from src.infra.repositories.movie import MovieRepository

movie_repository = MovieRepository()
fake = Faker()


def test_insert():
    # Fake payload
    fake_name = fake.word()

    # Inserting fake registry
    movie_repository.insert(name=fake_name)

    # Selecting fake registry
    query = movie_repository.select(name=fake_name, available=True)

    # Checking equalities
    assert query[0].name == fake_name
    assert query[0].available == True

    # Cleaning DB
    movie_repository.delete(id=(query[0].id))
