class VersionHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Lunch-Decision-API-Version'] = '1.0.0'  # version in headers
        return response
