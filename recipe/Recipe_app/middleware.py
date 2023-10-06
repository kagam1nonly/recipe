# middleware.py
from django.conf import settings
import requests

class WebpackDevServerProxyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for a static file or not
        if not request.path.startswith('/static/'):
            # Forward the request to the Webpack Dev Server
            webpack_dev_server_response = requests.get(
                f'{settings.WEBPACK_DEV_SERVER_PROXY}{request.path}'
            )
            return webpack_dev_server_response

        return self.get_response(request)