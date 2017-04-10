import sys
import urllib.request as urllib2

host = 'http://saweather.market.alicloudapi.com'
path = '/area-to-id'
method = 'GET'
appcode = '4bd498ca250b4a5ea430227fa1eb4768'
querys = 'area=%E4%B8%BD%E6%B1%9F'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
