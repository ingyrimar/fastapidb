from database import Base, engine
from models import Item

print("creating database ....")
Base.metadata.create_all(engine)