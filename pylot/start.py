import xmlrpclib
import xml2dict

host = 'http://localhost'
port = '3000'

server = xmlrpclib.Server('%s:%s' % (host, port))
response = server.start()

xml = xml2dict.XML2Dict()
r = xml.fromstring(response)

summary = r.results['summary-results']
#summary.requests
#summary.errors

print summary
