from src.auth.hashes import Hashes
from src.domain.dto.user import CreateUser
from src.infra.repositories.user import UserRepository

hashes = Hashes()
user_repository = UserRepository()


class UserService:
    def create(self, schema: CreateUser):
        formated_email = (schema.email).lower()
        formated_first_name = (schema.first_name).capitalize()
        formated_last_name = (schema.last_name).capitalize()
        hashed_password = hashes.generate_password_hash(
            password=(schema.password)
        )

        user_repository.insert(
            email=formated_email,
            first_name=formated_first_name,
            last_name=formated_last_name,
            password=hashed_password,
        )


test = UserService()
x = CreateUser(email='oi', first_name='oi', last_name='oi', password='oi')
test.create(schema=x)
