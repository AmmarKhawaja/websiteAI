from google_images_search import GoogleImagesSearch
import secret as s

def get_image(desc='Green screen', name='test'):

    gis = GoogleImagesSearch(s.GOOGLEIMAGES_API_KEY, s.GOOGLEIMAGES_CX_KEY)
    params = {
        'q': desc,
        'num': 1,
    }  
    gis.search(search_params=params, path_to_dir='.', custom_image_name='.\\images\\' + name)