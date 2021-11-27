import json
from datetime import date

from django.http import HttpResponse
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt


# Create your views here.
def download_sentinal_data(request):
    try:
        # connect to the API
        api = SentinelAPI('abbasgis', 'abbas123@abc', 'https://apihub.copernicus.eu/apihub')
        aoi = 'POINT (41.9 12.5)'
        products = api.query(aoi,
                             date=('20170801', '20170830'),
                             platformname='Sentinel-2',
                             cloudcoverpercentage=(0, 30))
        print(json.dumps(products, indent=4))
        for k in products:
            api.download(k)
        print(str(products))
        # api.download(products)
        product_id = '835405b7-2c17-4681-b743-fb9d7bb5591a'
        # download single scene by known product id
        api.download(product_id)

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
        return HttpResponse("Downloaded")
    except Exception as e:
        return HttpResponse(e.args)
