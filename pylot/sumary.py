import urllib2
import time
import threading
import httplib
import xmlrpclib
import xml2dict

serverlist = [('http://10.128.42.171','3000'),('http://10.128.42.160','3000'),('http://10.128.42.195','3000'),('http://10.128.42.180','3000')]

class GetResult(threading.Thread):
    def __init__(self, host, port = 3000):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.requests = 0
        self.errors = 0

    def run(self):
        server = xmlrpclib.Server('%s:%s' % (self.host, self.port))
        response = server.start(230,5)
        
        xml = xml2dict.XML2Dict()
        r = xml.fromstring(response)

        summary = r.results['summary-results']
        self.requests = summary['requests']['value']
        self.errors = summary['errors']['value']

total = 0
threads = []
for server in serverlist:
    t = GetResult(server[0],server[1])
    threads.append(t)
    t.start()


for t in threads:
    t.join()
    
for t in threads:
    total += int(t.requests)

print total