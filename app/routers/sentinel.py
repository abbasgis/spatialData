import datetime
from typing import Optional, List

from fastapi import APIRouter, Query

from starlette.requests import Request

# from app.routers.datatypes.sentinel import ItemProperties
from app.routers.datatypes.sentinel import SentinelDataInfo
from app.utils.sentinel import SentinelUtils

router = APIRouter(prefix="/v1", tags=["sentinel"])


@router.get("/download_by_product_id/{product_id}", description="Download the file by specified Sentinel product id")
def download_sentinel_data_by_productID(request: Request,
                                        product_id: str = "835405b7-2c17-4681-b743-fb9d7bb5591a"):
    sentinel_utils = SentinelUtils()
    sentinel_utils.download_by_product_id(product_id)
    return {"msg": "success"}


@router.post("/sentinel", description="Returns the sentinel download json file")
def download_sentinel_data(request: Request,
                           aoi: str = 'POINT (74 34)',
                           start_date: str = '20190801',
                           end_date: str = '20190830',
                           platformname: str = Query("Sentinel-2", enum=["Sentinel-2"]),
                           sentinal_data_info: SentinelDataInfo = None
                           ):
    SentinelDataInfo.aoi = aoi
    SentinelDataInfo.start_date = start_date
    SentinelDataInfo.end_date = end_date
    SentinelDataInfo.platformname = platformname
    sentinel_utils = SentinelUtils()
    return sentinel_utils.description
