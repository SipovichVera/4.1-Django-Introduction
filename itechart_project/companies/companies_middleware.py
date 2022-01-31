class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_view(self, request, *args) -> None:
        with open('/home/vera/Study/file_with_request.txt', 'w') as file:
            file.write(str(request.headers))
