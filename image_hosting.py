from imgurpython import ImgurClient
from api_credentials import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET

def upload_media_functions():
    client_id = IMGUR_CLIENT_ID
    client_secret = IMGUR_CLIENT_SECRET
    client = ImgurClient(client_id, client_secret)

    print client.get_account('jonathanoj')

upload_media_functions()