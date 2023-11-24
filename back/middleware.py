from django.http import Http404

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # 정의한 URL 패턴이 아니라면 404 에러 발생
        if not any(request.path_info.startswith(pattern) for pattern in ['/allowed/', '/another-allowed/']):
            raise Http404("Page not found")

        return response