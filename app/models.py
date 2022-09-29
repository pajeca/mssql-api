from sqlalchemy import Column, Date, String
from sqlalchemy.orm import relationship
from database import Base

metadata = Base.metadata

class SqlServer2017(Base):
    __tablename__ = 'sql_server_2017'
    __table_args__ = {'schema': 'mssql_builds'}

    sql_server = Column(String)
    version = Column(String)
    build = Column(String, primary_key=True)
    file_version = Column(String)
    description = Column(String)
    url_link = Column(String)
    release_date = Column(Date)
    is_latest = Column(String)
    next_build = Column(String)
    community_technology_preview = Column(String)
    cumulative_update = Column(String)
    hot_fix = Column(String)
    released_to_manufacturing = Column(String)


class SqlServer2019(Base):
    __tablename__ = 'sql_server_2019'
    __table_args__ = {'schema': 'mssql_builds'}

    sql_server = Column(String)
    version = Column(String)
    build = Column(String, primary_key=True)
    file_version = Column(String)
    description = Column(String)
    url_link = Column(String)
    release_date = Column(Date)
    is_latest = Column(String)
    next_build = Column(String)
    community_technology_preview = Column(String)
    cumulative_update = Column(String)
    hot_fix = Column(String)
    released_to_manufacturing = Column(String)


class SqlServer2022(Base):
    __tablename__ = 'sql_server_2022'
    __table_args__ = {'schema': 'mssql_builds'}

    sql_server = Column(String)
    version = Column(String)
    build = Column(String, primary_key=True)
    file_version = Column(String)
    description = Column(String)
    url_link = Column(String)
    release_date = Column(Date)
    is_latest = Column(String)
    next_build = Column(String)
    community_technology_preview = Column(String)
    cumulative_update = Column(String)
    hot_fix = Column(String)
    released_to_manufacturing = Column(String)