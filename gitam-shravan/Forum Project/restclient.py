import urllib.request,urllib.response,urllib.error,urllib.parse

values = {'forumname':'foo bar',
          'createdby':'jagan'
         }
databytes = urllib.parse.urlencode(values)

req = urllib.request.Request(url='http://localhost:8080/forums', data=databytes.encode('utf-8'))

f = urllib.request.urlopen(req)

print(f.read())






