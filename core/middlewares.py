class CORS:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "PUT, GET, HEAD, POST, DELETE, OPTIONS"
        response['Content-Type'] = "application/json"
        return response