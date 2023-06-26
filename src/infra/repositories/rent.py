from datetime import date
from typing import List

from src.infra.configs.session import session
from src.infra.entities.rent import Rent as RentEntity
from src.infra.repositories.errors.common import (IdNotFoundError,
                                                  ParamAreNotRecognizedError,
                                                  ParamIsNotDateError,
                                                  ParamIsNotStringError)


class Rent:
    def insert(
        self,
        id: str,
        user: str,
        customer: str,
        movie: str,
        devolution_date: date,
    ) -> RentEntity:
        # Trechos comentados devem ser implementados em services
        try:
            # data_insert = RentEntity(
            #     id=str(uuid.uuid1()),
            #     user=user.capitalize(),
            #     customer=customer.capitalize(),
            #     movie=movie.capitalize(),
            #     devolution_date=devolution_date
            # )

            if params_is_none(id, user, customer, movie, devolution_date):
                raise IncompleteParamsError
            if param_is_not_a_string(id, user, customer, movie):
                raise ParamIsNotStringError
            if param_is_not_a_date(devolution_date):
                raise ParamIsNotDateError(error_param=devolution_date)

            data_insert = RentEntity(
                id=id,
                user=user,
                customer=customer,
                movie=movie,
                devolution_date=devolution_date,
            )
            session.add(data_insert)
            session.commit()

            return data_insert

        except IncompleteParamsError as err:
            session.rollback()
            return err.message
        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        except ParamIsNotDateError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def select(
        self,
        id: str = None,
        user: str = None,
        customer: str = None,
        movie: str = None,
        rent_date: date = None,
        devolution_date: date = None,
        finished: bool = None,
    ) -> List[RentEntity]:
        try:
            custom_filter = session.query(RentEntity)
            if id is not None:
                if param_is_not_a_string(id):
                    raise ParamIsNotStringError
                custom_filter = custom_filter.filter(RentEntity.id == id)
            if user is not None:
                if param_is_not_a_string(user):
                    raise ParamIsNotStringError
                custom_filter = custom_filter.filter(RentEntity.user == user)
            if customer is not None:
                if param_is_not_a_string(customer):
                    raise ParamIsNotStringError
                custom_filter = custom_filter.filter(
                    RentEntity.customer == customer
                )
            if movie is not None:
                if param_is_not_a_string(movie):
                    raise ParamIsNotStringError
                custom_filter = custom_filter.filter(RentEntity.movie == movie)
            if rent_date is not None:
                if param_is_not_a_date(rent_date):
                    raise ParamIsNotDateError(error_param=rent_date)
                custom_filter = custom_filter.filter(
                    RentEntity.rent_date == rent_date
                )
            if devolution_date is not None:
                if param_is_not_a_date(devolution_date):
                    raise ParamIsNotDateError(error_param=devolution_date)
                custom_filter = custom_filter.filter(
                    RentEntity.devolution_date == devolution_date
                )
            if finished is not None:
                if param_is_not_a_bool(finished):
                    raise ParamIsNotDateError(error_param=finished)
                custom_filter = custom_filter.filter(
                    RentEntity.finished == finished
                )

            data_select = custom_filter.all()

            if data_select == []:
                return 'No data found'

            return data_select

        except Exception as err:
            return err
        finally:
            session.close()

    def update(self, id: str = None, **kwargs) -> RentEntity:
        """
        Args:
            user (str)
            customer (str)
            movie (str)
            devolution_date (datetime.datetime(YYYY, M, D))
            finished (bool)
        """
        rent_entity = RentEntity()
        try:
            if params_is_none(id):
                raise IncompleteParamsError
            if param_is_not_a_string(id):
                raise ParamIsNotStringError
            if id_not_found(session=session, object=RentEntity, arg=id):
                raise IdNotFoundError(id=id)
            for kwarg in kwargs:
                if param_is_not_a_recognized_attribute(
                    object=rent_entity, arg=kwarg
                ):
                    raise ParamAreNotRecognizedError(error_param=kwarg)
                session.query(RentEntity).filter(RentEntity.id == id).update(
                    {f'{kwarg}': kwargs[f'{kwarg}']}
                )
            data_update = (
                session.query(RentEntity).filter(RentEntity.id == id).first()
            )
            return data_update

        except IncompleteParamsError as err:
            session.rollback()
            return err.message
        except ParamIsNotStringError as err:
            session.rollback()
            return err.message
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        except ParamAreNotRecognizedError as err:
            session.rollback()
            return err.message
        finally:
            session.close()

    def delete(self, id: str) -> RentEntity:
        try:

            if id_not_found(session=session, object=RentEntity, arg=id):
                raise IdNotFoundError(id=id)

            data_delete = (
                session.query(RentEntity).filter(RentEntity.id == id).first()
            )

            session.query(RentEntity).filter(RentEntity.id == id).delete()
            session.commit()

            return data_delete

        except IdNotFoundError as err:
            session.rollback()
            return err.message
        finally:
            session.close()
