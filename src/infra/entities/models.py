from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f'User (id = {self.id}, email = {self.email}, name = {self.name}, is_active = {self.is_active})'


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f'Customer (id = {self.id}, email = {self.email}, name = {self.name}, is_active = {self.is_active})'


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    available = Column(Boolean, default=True)

    def __repr__(self):
        return f'Movie (id = {self.id}, name = {self.name}, available = {self.available})'


class Rent(Base):
    __tablename__ = 'rents'

    id = Column(String, primary_key=True)
    user = Column(String, ForeignKey('users.id'))
    customer = Column(String, ForeignKey('customers.id'))
    movie = Column(String, ForeignKey('movies.id'))
    rent_date = Column(DateTime(timezone=True), server_default=func.now())
    devolution_date = Column(DateTime(timezone=True), default=None)
    finished = Column(Boolean, default=True)
