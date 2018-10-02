import requests



session = requests.Session()
proxies = {}
api_url = "http://cardinal.mlsquare.io"


api_login = self.api_call("/users/login", data=credentials, authed=False)
token = api_login["token"]
user_id = api_login["id"]