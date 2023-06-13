from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, func

from src.infra.configs.base import Base


class Rent(Base):
    __tablename__ = 'rents'

    id = Column(String, primary_key=True)
    user = Column(String, ForeignKey('users.id'))
    customer = Column(String, ForeignKey('customers.id'))
    movie = Column(String, ForeignKey('movies.id'))
    rent_date = Column(DateTime(timezone=True), server_default=func.now())
    devolution_date = Column(DateTime(timezone=True), default=None)
    finished = Column(Boolean, default=True)
