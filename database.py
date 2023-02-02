# db name is ---->    'pizza_delivery_app'

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:123456@localhost:5432/pizza_delivery_app',
                       echo=True
                       )

Base = declarative_base()

Session = sessionmaker()