from sqlalchemy import Boolean, Column, String

from src.infra.configs.base import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    available = Column(Boolean, default=True)

    def __repr__(self):
        return f'Movie (id = {self.id}, name = {self.name}, available = {self.available})'
