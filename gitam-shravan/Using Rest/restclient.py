import urllib2
import urllib

values = {'forumname':'foo bar',
'createdby':'jagan'
}
databytes = urllib.urlencode(values)
req = urllib2.Request(url='http://localhost:8080/forums',data=databytes.encode('utf-8'))
f = urllib2.urlopen(req)
print(f.read())
