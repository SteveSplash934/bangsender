from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    Includes AsyncAttrs for async compatibility.
    """
    pass

# Import models here so Alembic can see them!
# (We will import this Base in alembic/env.py)