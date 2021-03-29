# required Libraries 
import google_streetview.api
import google_streetview.helpers

lat_north = 42.0451 
""" Evanston """
lat_south = 41.8919 
"""(navy pier) """

long_east = -87.6051 
"""(navy pier)"""
long_west = -88.0073 

increment = 0.4

download_data_dir = "./GSV_images"

def get_images(lat_north, lat_south, long_east, long_west, increment, api_key, data_dir):
    lat_difference = increment/69
    long_differnece = increment/54

    # making a list of all the latitude and longitude intersections 

    lat = lat_south
    lon = long_east

    cordinates = []

    while lat <= lat_north:
        while lon <= long_east:
            temp = str(lat) +','+str(lon)+';'
            cordinates.append(temp)
            lon += long_differnece
        lon = long_west
        lat = lat + lat_difference

    API_locations = ''.join(cordinates)

    apiargs = {
        'location': API_locations,
        'size': '640x640',
        'heading': '0;90;180;270',
        'fov': '90;120',
        'pitch': '0',
        'key' : api_key
        }

    # Get a list of all possible queries from multiple parameters
    api_list = google_streetview.helpers.api_list(apiargs)

    print( 'api_list done!')

    # Create a results object for all possible queries provides metadata 
    # of downloaded images
    results = google_streetview.api.results(api_list)

    print("downloading starting")

    # Download images to directory 'downloads'
    results.download_links(data_dir)

    print("downloading done")


get_images(lat_north, lat_south, long_east, long_west, increment, api_key="", data_dir=download_data_dir)