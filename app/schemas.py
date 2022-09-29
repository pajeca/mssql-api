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
    release_date: Optional[date]
    is_latest: Optional[bool]
    next_build: Optional[str]
    community_technology_preview: Optional[bool]
    cumulative_update: Optional[bool]
    hot_fix: Optional[bool]
    released_to_manufacturing: Optional[bool]

    class Config:
        orm_mode = True

