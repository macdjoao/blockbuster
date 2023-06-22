from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)

from src.infra.configs.base import Base


class Rent(Base):
    __tablename__ = 'rents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rent_date = Column(DateTime(timezone=True), server_default=func.now())
    devolution_date = Column(DateTime(timezone=True), default=None)
    finished = Column(Boolean, default=True)

    def __repr__(self):
        return f'Rent (id = {self.id}, user_id = {self.user_id}, customer_id = {self.customer_id}, movie_id = {self.movie_id}, rent_date = {self.rent_date}, devolution_date = {self.devolution_date}, finished = {self.finished})'
