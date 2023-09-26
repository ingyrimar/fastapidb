from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://item_db_77cq_user:pmKeR0xcazJ4IvHj1mMn0gKMqOJGBszI@dpg-ck8t44c7m7is73aki8kg-a.ohio-postgres.render.com/item_db_77cq",
          echo=True             
        )

Base=declarative_base()
SessionLocal= sessionmaker(engine)