from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from main import app


e = create_engine(app.config['DATABASE'], echo=app.config['DEBUG'])
Base = declarative_base()
Session = sessionmaker(bind=e)
session = Session()
