from typing import List

from src.auth.hashes import Hashes
from src.domain.dto.user import CreatedUser, CreateUser
from src.infra.repositories.user import UserRepository

hashes = Hashes()
user_repository = UserRepository()


class UserService:
    def create(self, schema: CreateUser):
        try:
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

            data_select = user_repository.select(
                email=formated_email,
                first_name=formated_first_name,
                last_name=formated_last_name,
            )

            return CreatedUser(
                id=data_select[0].id,
                email=data_select[0].email,
                first_name=data_select[0].first_name,
                last_name=data_select[0].last_name,
                is_active=data_select[0].is_active,
            )

        except Exception as err:
            return err


test = UserService()
x = CreateUser(email='opawq', first_name='oi', last_name='oi', password='oi')
print(test.create(schema=x))
