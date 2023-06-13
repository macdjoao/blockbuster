from src.infra.configs.session import session
from src.infra.entities.movie import Movie as MovieEntity


class Movie:
    def insert(self, id: str, name: str):
        # Trechos comentados devem ser implementados em services
        try:
            # data_insert = MovieEntity(
            #     id=str(uuid.uuid1()),
            #     email=email.lower(),
            #     name=name.capitalize(),
            # )
            data_insert = MovieEntity(
                id=id,
                name=name,
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except Exception as err:
            session.rollback()
            return err
        finally:
            session.close()
