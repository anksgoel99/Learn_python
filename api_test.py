import requests
from requests_oauthlib import OAuth1
url = "https://simplivity@15.112.66.151:443/api/oauth/token"
data = {"grant_type":"password"}
username =  "administrator@vsphere.local"
password = "12ISO*help"
out = requests.get(url,data=data, auth=OAuth1(username, password))
print out

