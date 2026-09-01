from sqlmodel import SQLModel, create_engine, Field, Session

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = Field(default=None)


postgres_url = "postgresql://postgres:4434642@localhost:5432/sqlmodel"
engine = create_engine(postgres_url, echo=True)

def create_data_base_and_tables(): #this prevents the side effects when importing something from  app.py file.    
    SQLModel.metadata.create_all(engine)

def get_heroes():
    hero1 = Hero(name="Deadpond", secret_name="Dive Wilson", age=100)
    hero2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero1)
        session.add(hero2)
        session.add(hero3)
        session.commit()
        session.close()

def main():
    create_data_base_and_tables()
    get_heroes()


if __name__ == "__main__": #this helps as to call our self intentionally when we need to create the database and tables.
    main()