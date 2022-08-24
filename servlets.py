import asyncio
import logging

from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web import static

from resources import AStreamHandlerResource, AHtmlHandlerResource, MP4HandlerResource, ABigHtmlHandlerResource

logger = logging.getLogger(__name__)


class ClientApiHttpServer:
    def __init__(self, component):
        self.component = component

        root = Resource()
        root.putChild(b"static", static.File('./static_dir'))
        root.putChild(b"stream", AStreamHandlerResource(component))
        root.putChild(b"html", AHtmlHandlerResource(component))
        root.putChild(b"html-big", ABigHtmlHandlerResource(component))
        root.putChild(b"video", MP4HandlerResource(component))
        self.factory = Site(root)
        # self.factory.displayTracebacks = False

    def setup(self, port):
        http_port = port
        interface = '0.0.0.0'
        logger.info("Starting API HTTP server on %s%d", http_port)
        self.component.reactor.listenTCP(http_port, self.factory, interface=interface)


class Component:
    def __init__(self, custom_reactor, port):
        self.reactor = custom_reactor
        self.port = port
        self.api = ClientApiHttpServer(self)

    def run(self):
        self.api.setup(self.port)
        asyncio.set_event_loop(self.reactor._asyncioEventloop)
        self.reactor.run()
