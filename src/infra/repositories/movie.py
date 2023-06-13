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

    def select(
        self,
        id: str = None,
        name: str = None,
        available: bool = None,
    ):
        try:
            custom_filter = session.query(MovieEntity)
            if id is not None:
                custom_filter = custom_filter.filter(MovieEntity.id == id)
            if name is not None:
                custom_filter = custom_filter.filter(MovieEntity.name == name)
            if available is not None:
                custom_filter = custom_filter.filter(
                    MovieEntity.available == available
                )

            data_select = custom_filter.all()

            return data_select

        except Exception as err:
            return err
        finally:
            session.close()

    def update(
        self,
        id: str,
        name: str = None,
        available: bool = None,
    ):
        try:
            if name is not None:
                # user.update({'name': name.capitalize()})
                session.query(MovieEntity).filter(MovieEntity.id == id).update(
                    {'name': name}
                )
            if available is not None:
                session.query(MovieEntity).filter(MovieEntity.id == id).update(
                    {'is_active': available}
                )
            session.commit()

            data_update = (
                session.query(MovieEntity).filter(MovieEntity.id == id).first()
            )

            return data_update

        except Exception as err:
            session.rollback()
            return err
        finally:
            session.close()

    def delete(self, id: str):
        try:

            data_delete = (
                session.query(MovieEntity).filter(MovieEntity.id == id).first()
            )

            session.query(MovieEntity).filter(MovieEntity.id == id).delete()
            session.commit()

            return data_delete

        except Exception as err:
            session.rollback()
            return err
        finally:
            session.close()
