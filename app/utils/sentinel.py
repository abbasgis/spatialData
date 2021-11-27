from sentinelsat import SentinelAPI

from app.config.utils import ConfigUtils
from app.routers.datatypes.sentinel import SentinelDataInfo


class SentinelUtils:
    base_url: str
    description: {}
    sentinel_user: str
    sentinel_password: str
    api: SentinelAPI

    def __init__(self):
        config_utils = ConfigUtils()
        self.sentinel_user = config_utils.get_data('sentinel_user')
        self.sentinel_password = config_utils.get_data('sentinel_password')
        self.api = SentinelAPI(self.sentinel_user, self.sentinel_password, 'https://apihub.copernicus.eu/apihub')
        self.download_by_aoi()

    def download_by_aoi(self):
        aoi = SentinelDataInfo.aoi
        products = self.api.query(aoi,
                                  date=(SentinelDataInfo.start_date, SentinelDataInfo.end_date),
                                  platformname=SentinelDataInfo.platformname,
                                  cloudcoverpercentage=(0, 30))
        self.description = products
        # print(json.dumps(products, indent=4))
        # for k in products:
        #     self.api.download(k)
        # print(str(products))

    def download_by_product_id(self, product_id):
        # product_id='835405b7-2c17-4681-b743-fb9d7bb5591a'
        # download single scene by known product id
        self.api.download(product_id)

        # # search by polygon, time, and Hub query keywords
        # footprint = geojson_to_wkt(read_geojson('map.geojson'))
        # products = api.query(footprint,
        #                      date=('20151219', date(2015, 12, 29)),
        #                      platformname='Sentinel-2',
        #                      cloudcoverpercentage=(0, 30))
        #
        # # download all results from the search
        # api.download_all(products)
        #
        # # GeoJSON FeatureCollection containing footprints and metadata of the scenes
        # api.to_geojson(products)
        #
        # # GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
        # api.to_geodataframe(products)
        #
        # # Get basic information about the product: its title, file size, MD5 sum, date, footprint and
        # # its download url
        # api.get_product_odata(product_id)
        #
        # # Get the product's full metadata available on the server
        # api.get_product_odata(product_id, full=True)
