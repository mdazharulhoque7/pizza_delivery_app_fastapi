from database import engine, Base
from models.user import User
from models.order import Order

Base.metadata.create_all(bind=engine)
