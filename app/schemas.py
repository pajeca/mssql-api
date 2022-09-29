from typing import List, Optional, Generic
from pydantic import BaseModel
from datetime import date

class BuildGet(BaseModel):
    sql_server: str
    build: str

    class Config:
        orm_mode = True

class BuildResponse(BaseModel):
    sql_server: str
    version: str
    build: str
    file_version: str
    description: str
    url_link: Optional[str]
    release_date: date
    is_latest: Optional[str]
    next_build: Optional[str]
    community_technology_preview: Optional[str]
    cumulative_update: Optional[str]
    hot_fix: Optional[str]
    released_to_manufacturing: Optional[str]

    class Config:
        orm_mode = True

