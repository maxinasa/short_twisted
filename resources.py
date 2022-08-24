import asyncio
import logging

from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET

logger = logging.getLogger(__name__)
CHUNK_SIZE = 2**16*20


class AStreamHandlerResource(Resource):

    def __init__(self, component):
        super().__init__()
        self.component = component

    def render_GET(self, request):
        # Any additional headers we might need
        # request.setHeader("Access-Control-Allow-Origin", "*")
        # request.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT")
        # request.setHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        request.setHeader("Content-Type", "application/json; charset=UTF-8")

        self._async_render(request)
        return NOT_DONE_YET

    @staticmethod
    async def something(request):
        logger.info(request)

        for idx in range(31):
            await asyncio.sleep(1)
            c = f"{chr(65 + idx)}"
            data = c * CHUNK_SIZE
            print(data)
            request.write(bytes(data, 'utf-8'))
        request.finish()

    def _async_render(self, request):
        asyncio.ensure_future(
            self.something(request),
            loop=asyncio.get_event_loop()
        )


class AHtmlHandlerResource(Resource):

    def __init__(self, component):
        super().__init__()
        self.component = component

    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html; charset=UTF-8")

        file_name = 'static_dir/page.html'
        with open(file_name, 'rb') as f:
            return f.read()


class ABigHtmlHandlerResource(Resource):

    def __init__(self, component):
        super().__init__()
        self.component = component

    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html; charset=UTF-8")

        file_name = 'static_dir/big_page.html'
        with open(file_name, 'rb') as f:
            return f.read()


class MP4HandlerResource(Resource):

    def __init__(self, component):
        super().__init__()
        self.component = component

    def render_GET(self, request):
        request.setHeader("Content-Type", "video/mp4; charset=UTF-8")

        return b''
