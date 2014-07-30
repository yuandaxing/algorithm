import re
import urllib2
import urllib
import os 
import urlparse
queue = []
queue.append('http://jandan.net/ooxx')
old = False
while len(queue) and not old  :
    url = queue.pop(0)
    connect = urllib2.urlopen(url)
    content = connect.read()
    for m in re.findall(r'''\<p\>\<img src="([^"]+)\"''', content) :
        print m
        result=urlparse.urlparse(m)
        localImg = 'C:/TDDOWNLOAD/jandan/'+result.path
        dirName = os.path.dirname(localImg)
        if not os.path.exists(dirName) : os.makedirs(dirName)
        try :
            localFile = 'C:/TDDOWNLOAD/jandan/'+result.path
            if os.path.exists(localFile) :
                old = True
                break
            urllib.urlretrieve(m, localFile)
        except Exception as e:
            print e
    nextPage = re.findall(r'''<a class="previous-comment-page" href="([^"]+)"''', content)[0]
    print nextPage
    queue.append(nextPage)
