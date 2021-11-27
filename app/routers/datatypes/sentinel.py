import datetime
from typing import Optional, Any, List, Union

from pydantic import BaseModel


class SentinelDataInfo(BaseModel):
    aoi: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    platformname: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "aoi": "POINT (74 32)",
                "start_date": "20190801",
                "end_date": "20190830",
                "platformname": "Sentinel-2"
            }
        }
