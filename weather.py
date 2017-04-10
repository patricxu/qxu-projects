import urllib, urllib2, sys


host = 'http://saweather.market.alicloudapi.com'
path = '/area-to-id'
method = 'GET'
appcode = '你自己的AppCode'
querys = 'area=%E4%B8%BD%E6%B1%9F'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
