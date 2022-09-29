#!/usr/bin/env python3
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#@app.get('/')
#async def hello():
#    return {"message": "Hello World"}

@app.get("/{version}/all", response_model=list[schemas.BuildResponse])
async def get_version_all(version: str, db: Session = Depends(get_db)):
    version_out = crud.get_version_all(db, version=version)
    if version_out is None:
        raise HTTPException(status_code=404, detail="Version not found")
    return version_out

@app.get("/{version}/{build}", response_model=schemas.BuildResponse)
async def read_build(version: str, build: str, db: Session = Depends(get_db)):
    build_out = crud.get_build(db, version=version, build=build)
    if build_out is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return build_out