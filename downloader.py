# use bing-image-downloader

from bing_image_downloader import downloader

downloader.download('rose flower',limit =50, output_dir="/rose flower",adult_filter_off = True,force_replace = False, timeout=60)

#do similar for all other flowers