import datetime
from typing import Optional, List

from fastapi import APIRouter, Query

from starlette.requests import Request

# from app.routers.datatypes.landsat import ItemProperties
from app.routers.datatypes.landsat import LandsatDataInfo
from app.utils.landsat import LandsatUtils

router = APIRouter(prefix="/v1", tags=["landsat"])


@router.post("/landsat", description="Returns the landsat download json file")
def download_landsat_data(request: Request,
                          dataset: str = Query("landsat_tm_c1", enum=["landsat_tm_c1"]),
                          latitude: float = 32,
                          longitude: float = 72,
                          start_date: str = '2020-01-01',
                          end_date: str = '2020-10-01',
                          max_cloud_cover: int = 10,
                          landsat_data_info: LandsatDataInfo = None
                          ):
    LandsatDataInfo.latitude = latitude
    LandsatDataInfo.longitude = longitude
    LandsatDataInfo.start_date = start_date
    LandsatDataInfo.end_date = end_date
    LandsatDataInfo.max_cloud_cover = max_cloud_cover
    LandsatDataInfo.dataset = dataset
    landsat_utils = LandsatUtils()
    return landsat_utils.response
