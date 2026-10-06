#!/usr/bin/python3
"""Defines the State class and the Base instance used to map
Python classes to MySQL tables with SQLAlchemy."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state and links it to the MySQL table states. """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
