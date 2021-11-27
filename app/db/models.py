from sqlalchemy import Column, String, Boolean, Integer, JSON, DateTime, INTEGER, Sequence, desc

from app.db.database import Base, get_db, SessionLocal, get_raw_query_rs
from app.utils.common import DataLogger


# class SpatialDataInfo(Base):
#     __tablename__ = "spatial_data_info"
#     # id = Column(Integer, nullable=True)

