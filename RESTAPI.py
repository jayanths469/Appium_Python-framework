import requests
import simplejson
import jsonpath

url = "https://api.appcenter.ms/v0.1/orgs/UTCBIS/users/sunkarj/apps"
Responseofurl = requests.get(url)
print(Responseofurl)
Contentofurl = Responseofurl.content
print(Contentofurl)


