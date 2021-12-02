import datetime
from typing import Optional, Any, List, Union

from pydantic import BaseModel


class LandsatDataInfo(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]
    max_cloud_cover: Optional[int]
    start_date: Optional[str]
    end_date: Optional[str]
    dataset: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "dataset": "landsat_tm_c1",
                "latitude": "32",
                "longitude": "72",
                "start_date": "2020-01-01",
                "end_date": '2020-10-01',
                "max_cloud_cover": 10

            }
        }
