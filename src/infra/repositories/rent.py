from datetime import date
from typing import List

from src.infra.configs.session import session
from src.infra.entities.rent import Rent as RentEntity
from src.infra.repositories.errors.general import (IdNotFoundError,
                                                   IncompleteParamsError,
                                                   ParamAreNotRecognizedError)
from src.infra.repositories.utils.general import (
    id_not_found, param_is_not_a_recognized_attribute, params_is_none)


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

        except Exception as err:
            session.rollback()
            return err
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
                custom_filter = custom_filter.filter(RentEntity.id == id)
            if user is not None:
                custom_filter = custom_filter.filter(RentEntity.user == user)
            if customer is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.customer == customer
                )
            if movie is not None:
                custom_filter = custom_filter.filter(RentEntity.movie == movie)
            if rent_date is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.rent_date == rent_date
                )
            if devolution_date is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.devolution_date == devolution_date
                )
            if finished is not None:
                custom_filter = custom_filter.filter(
                    RentEntity.finished == finished
                )

            data_select = custom_filter.all()

            return data_select

        except Exception as err:
            return err
        finally:
            session.close()

    def update(self, id: str = None, **kwargs) -> RentEntity:
        """
        **kwargs(
            user: str
            customer: str
            movie: str
            devolution_date: datetime.datetime(YYYY, M, D)
            finished: bool
        )
        """
        rent_entity = RentEntity()
        try:
            if params_is_none(id):
                raise IncompleteParamsError
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
        except IdNotFoundError as err:
            session.rollback()
            return err.message
        except ParamAreNotRecognizedError as err:
            session.rollback()
            return err.message
        finally:
            session.close()
