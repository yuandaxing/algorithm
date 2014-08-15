import re
import urllib2
import urllib
import os 
import urlparse
queue = []
queue.append('http://jandan.net/ooxx')
localPath = 'C:/Users/dayua/TDDOWNLOAD/jandan'
old = False
while len(queue) and not old  :
    url = queue.pop(0)
    connect = urllib2.urlopen(url)
    content = connect.read()
    for m in re.findall(r'''\<p\>\<img src="([^"]+)\"''', content) :
        print m
        result=urlparse.urlparse(m)
        localImg = localPath + result.path
        dirName = os.path.dirname(localImg)
        if not os.path.exists(dirName) : os.makedirs(dirName)
        try :
            if os.path.exists(localImg) :
                old = True
                print localImg, 'already existing'
                break
            urllib.urlretrieve(m, localImg)
        except Exception as e:
            print e
    nextPage = re.findall(r'''<a class="previous-comment-page" href="([^"]+)"''', content)[0]
    print nextPage
    queue.append(nextPage)

command = 'find ' + localPath +'''  -name '*.jpg' -o -name '*.gif' -o -name '*.JPG' -o -name '*.png' -exec cp -n {} /cygdrive/c/develop/django/static/picture_slide/ \; '''

print command 
print os.system(command)
