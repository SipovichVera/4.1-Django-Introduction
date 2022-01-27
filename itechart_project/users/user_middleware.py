class Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response
        
    def process_view(self, request, *args):
        print(request.user.is_superuser, 1)
        if request.user.is_superuser:
            request.user.is_admin = True