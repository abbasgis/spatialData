from landsatxplore.api import API
from sentinelsat import SentinelAPI

from app.config.utils import ConfigUtils
from app.routers.datatypes.landsat import LandsatDataInfo


class LandsatUtils:
    base_url: str
    response: {}
    sentinel_user: str
    sentinel_password: str
    api: API

    def __init__(self):
        config_utils = ConfigUtils()
        self.landsat_user = config_utils.get_data('landsat_user')
        self.landsat_password = config_utils.get_data('landsat_password')
        self.api = API(self.landsat_user, self.landsat_password, )
        self.download_landsat_scenes()

    def download_landsat_scenes(self):
        # Search for Landsat TM scenes
        scenes = self.api.search(
            dataset='landsat_tm_c1',
            latitude=LandsatDataInfo.latitude,
            longitude=-LandsatDataInfo.longitude,
            start_date=LandsatDataInfo.start_date,
            end_date=LandsatDataInfo.end_date,
            max_cloud_cover=LandsatDataInfo.max_cloud_cover
        )
        print(f"{len(scenes)} scenes found.")
        self.response = {}
