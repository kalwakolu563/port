from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./leads.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_table():
    from models import Lead
    Lead.metadata.create_all(bind=engine)
