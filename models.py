from database import Base
from sqlalchemy import Text, Column, String, Boolean, Integer

class Item(Base):
    __tablename__='items'
    id=Column(Integer, primary_key=True)
    name=Column(String(225), nullable=False, unique=True)
    price=Column(Integer, nullable=False)
    description=Column(Text)
    on_offer=Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
    