from django.views import View
from django.http import HttpResponse


class LoginView(View):
    def get(self, request):
        return HttpResponse("这是get请求")

    def post(self, request):
        return HttpResponse("这是post请求")


# Create your views here.
