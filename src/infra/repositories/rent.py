import datetime
from datetime import date
from typing import List

from src.infra.configs.session import session
from src.infra.entities.customer import Customer as CustomerEntity
from src.infra.entities.movie import Movie as MovieEntity
from src.infra.entities.rent import Rent as RentEntity
from src.infra.entities.user import User as UserEntity
from src.infra.repositories.errors.common import (IdNotFoundError,
                                                  ParamAreNotRecognizedError,
                                                  ParamIsNotBoolError,
                                                  ParamIsNotDateError,
                                                  ParamIsNotIntegerError,
                                                  ParamIsNotStringError)


class RentRepository:
    def insert(
        self,
        user_id: int,
        customer_id: int,
        movie_id: int,
        devolution_date: date,
    ) -> RentEntity:
        try:
            if type(user_id) is not int:
                raise ParamIsNotIntegerError(arg=user_id)
            if type(customer_id) is not int:
                raise ParamIsNotIntegerError(arg=customer_id)
            if type(movie_id) is not int:
                raise ParamIsNotIntegerError(arg=movie_id)
            if type(devolution_date) is not datetime.datetime:
                raise ParamIsNotDateError(arg=devolution_date)

            data_user = (
                session.query(UserEntity)
                .filter(UserEntity.id == user_id)
                .first()
            )
            if data_user is None:
                raise IdNotFoundError(id=user_id)

            data_customer = (
                session.query(CustomerEntity)
                .filter(CustomerEntity.id == customer_id)
                .first()
            )
            if data_customer is None:
                raise IdNotFoundError(id=customer_id)

            data_movie = (
                session.query(MovieEntity)
                .filter(MovieEntity.id == movie_id)
                .first()
            )
            if data_movie is None:
                raise IdNotFoundError(id=movie_id)

            data_insert = RentEntity(
                user_id=user_id,
                customer_id=customer_id,
                movie_id=movie_id,
                devolution_date=devolution_date,
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except ParamIsNotDateError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def select(
        self,
        id: int = None,
        user_id: int = None,
        customer_id: int = None,
        movie_id: int = None,
        rent_date: date = None,
        devolution_date: date = None,
        finished: bool = None,
    ) -> List[RentEntity]:
        try:
            custom_filter = session.query(RentEntity)

            if id is not None:
                if type(id) is not int:
                    raise ParamIsNotIntegerError(arg=id)
                custom_filter = custom_filter.filter(RentEntity.id == id)

            if user_id is not None:
                if type(user_id) is not int:
                    raise ParamIsNotIntegerError(arg=user_id)
                custom_filter = custom_filter.filter(
                    RentEntity.user_id == user_id
                )

            if customer_id is not None:
                if type(customer_id) is not int:
                    raise ParamIsNotIntegerError(arg=customer_id)
                custom_filter = custom_filter.filter(
                    RentEntity.customer_id == customer_id
                )

            if movie_id is not None:
                if type(movie_id) is not int:
                    raise ParamIsNotIntegerError(arg=movie_id)
                custom_filter = custom_filter.filter(
                    RentEntity.movie_id == movie_id
                )

            if rent_date is not None:
                if type(rent_date) is not datetime.datetime:
                    raise ParamIsNotDateError(arg=rent_date)
                custom_filter = custom_filter.filter(
                    RentEntity.rent_date == rent_date
                )

            if devolution_date is not None:
                if type(devolution_date) is not datetime.datetime:
                    raise ParamIsNotDateError(arg=devolution_date)
                custom_filter = custom_filter.filter(
                    RentEntity.devolution_date == devolution_date
                )

            if finished is not None:
                if type(finished) is not bool:
                    raise ParamIsNotBoolError(arg=finished)
                custom_filter = custom_filter.filter(
                    RentEntity.finished == finished
                )

            data_select = custom_filter.all()
            return data_select

        except ParamIsNotIntegerError as err:
            return err.message
        except ParamIsNotDateError as err:
            return err.message
        except ParamIsNotBoolError as err:
            return err.message
        finally:
            session.close()

    def update(
        self,
        id: int,
        user_id: int = None,
        customer_id: int = None,
        movie_id: int = None,
        rent_date: date = None,
        devolution_date: date = None,
        finished: bool = None,
    ) -> RentEntity:
        try:
            if type(id) is not int:
                raise ParamIsNotIntegerError(arg=id)
            data_id = (
                session.query(RentEntity).filter(RentEntity.id == id).first()
            )
            if data_id is None:
                raise IdNotFoundError(id=id)

            if user_id is not None:
                if type(user_id) is not int:
                    raise ParamIsNotIntegerError(arg=user_id)
                data_user = (
                    session.query(UserEntity)
                    .filter(UserEntity.id == user_id)
                    .first()
                )
                if data_user is None:
                    raise IdNotFoundError(id=user_id)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {'user_id': user_id}
                )

            if customer_id is not None:
                if type(customer_id) is not int:
                    raise ParamIsNotIntegerError(arg=customer_id)
                data_customer = (
                    session.query(CustomerEntity)
                    .filter(CustomerEntity.id == customer_id)
                    .first()
                )
                if data_customer is None:
                    raise IdNotFoundError(id=customer_id)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {'customer_id': customer_id}
                )

            if movie_id is not None:
                if type(movie_id) is not int:
                    raise ParamIsNotIntegerError(arg=movie_id)
                data_movie = (
                    session.query(MovieEntity)
                    .filter(MovieEntity.id == movie_id)
                    .first()
                )
                if data_movie is None:
                    raise IdNotFoundError(id=movie_id)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {'movie_id': movie_id}
                )

            if rent_date is not None:
                if type(rent_date) is not datetime.datetime:
                    raise ParamIsNotDateError(arg=rent_date)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {'rent_date': rent_date}
                )

            if devolution_date is not None:
                if type(devolution_date) is not datetime.datetime:
                    raise ParamIsNotDateError(arg=devolution_date)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {'devolution_date': devolution_date}
                )

            if finished is not None:
                if type(finished) is not bool:
                    raise ParamIsNotBoolError(arg=finished)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {'finished': finished}
                )

            session.commit()

            data_update = (
                session.query(RentEntity).filter(RentEntity.id == id).first()
            )
            return data_update

        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except ParamIsNotDateError as err:
            session.rollback()
            return err.message
        except ParamIsNotBoolError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, id: int) -> RentEntity:
        try:

            if type(id) is not int:
                raise ParamIsNotIntegerError(arg=id)

            data_delete = (
                session.query(RentEntity).filter(RentEntity.id == id).first()
            )

            if data_delete is None:
                raise IdNotFoundError(arg=id)

            session.query(RentEntity).filter(RentEntity.id == id).delete()
            session.commit()

            return data_delete

        except ParamIsNotIntegerError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()
