from src.infra.configs.session import session
from src.infra.entities.movie import Movie as MovieEntity
from src.infra.repositories.errors.common import (IdNotFoundError,
                                                  ParamIsNotBoolError,
                                                  ParamIsNotIntegerError,
                                                  ParamIsNotStringError)


class MovieRepository:
    def insert(self, name: str):
        try:
            if type(name) is not str:
                raise ParamIsNotStringError(arg=name)

            data_insert = MovieEntity(
                name=name,
            )
            session.add(data_insert)
            session.commit()
            return data_insert

        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def select(
        self,
        id: int = None,
        name: str = None,
        available: bool = None,
    ):
        try:
            custom_filter = session.query(MovieEntity)

            if id is not None:
                if type(id) is not int:
                    raise ParamIsNotIntegerError(arg=id)
                custom_filter = custom_filter.filter(MovieEntity.id == id)

            if name is not None:
                if type(name) is not str:
                    raise ParamIsNotStringError(arg=name)
                custom_filter = custom_filter.filter(MovieEntity.name == name)

            if available is not None:
                if type(available) is not bool:
                    raise ParamIsNotBoolError(arg=available)
                custom_filter = custom_filter.filter(
                    MovieEntity.available == available
                )

            data_select = custom_filter.all()
            return data_select

        except ParamIsNotIntegerError as err:
            return err.message
        except ParamIsNotStringError as err:
            return err.message
        except ParamIsNotBoolError as err:
            return err.message
        finally:
            session.close()

    def update(
        self,
        id: int,
        name: str = None,
        available: bool = None,
    ):
        try:
            if type(id) is not int:
                raise ParamIsNotIntegerError(arg=id)
            data_id = (
                session.query(MovieEntity).filter(MovieEntity.id == id).first()
            )
            if data_id is None:
                raise IdNotFoundError(id=id)

            if name is not None:
                if type(name) is not str:
                    raise ParamIsNotStringError(arg=name)
                session.query(MovieEntity).filter(MovieEntity.id == id).update(
                    {'name': name}
                )

            if available is not None:
                if type(available) is not bool:
                    raise ParamIsNotBoolError(arg=available)
                session.query(MovieEntity).filter(MovieEntity.id == id).update(
                    {'is_active': available}
                )

            session.commit()

            data_update = (
                session.query(MovieEntity).filter(MovieEntity.id == id).first()
            )
            return data_update

        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        except ParamIsNotBoolError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, id: int):
        try:

            if type(id) is not int:
                raise ParamIsNotIntegerError(arg=id)

            data_id = (
                session.query(MovieEntity).filter(MovieEntity.id == id).first()
            )
            if data_id is None:
                raise IdNotFoundError(id=id)

            session.query(MovieEntity).filter(MovieEntity.id == id).delete()
            session.commit()
            return data_id

        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()
