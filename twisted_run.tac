from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from twisted.web import server
from metax.wsgi import application as application

resource = WSGIResource(reactor, reactor.getThreadPool(), application)
site = server.Site(resource)
reactor.listenTCP(8002, site)
reactor.run()