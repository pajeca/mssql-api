from sqlalchemy.orm import Session
import models, schemas

def get_build(db: Session, version: str, build: str):
    if version == "2017":
        return db.query(models.SqlServer2017).filter(models.SqlServer2017.build == build).first()    
    
    if version == "2022":
        return db.query(models.SqlServer2022).filter(models.SqlServer2022.build == build).first()
    
    if version == "2019":
        return db.query(models.SqlServer2019).filter(models.SqlServer2019.build == build).first()

def get_version_all(db: Session, version: str, skip: int = 0, limit: int = 200):
    if version == "2017":
        return db.query(models.SqlServer2017).offset(skip).limit(limit).all()
    
    if version == "2019":
        return db.query(models.SqlServer2019).offset(skip).limit(limit).all()
    
    if version == "2022":
        return db.query(models.SqlServer2022).offset(skip).limit(limit).all()