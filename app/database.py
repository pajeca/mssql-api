#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from local_settings import postgresql as settings

def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad local_settings file')
    
    return get_engine(settings['pguser'], settings['pgpasswd'], settings['pghost'], settings['pgport'], settings['pgdb'])

def get_session():
    engine = get_engine_from_settings()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    return SessionLocal


engine = get_engine_from_settings()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()