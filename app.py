from sqlmodel import SQLModel, create_engine, Field

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = Field(default=None)


postgres_url = "postgresql://postgres:4434642@localhost:5432/sqlmodel"
engine = create_engine(postgres_url, echo=True)

def create_data_base_and_tables(): #this prevents the side effects when importing something from  app.py file.    
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__": #this helps as to call our self intentionally when we need to create the database and tables.
    create_data_base_and_tables()