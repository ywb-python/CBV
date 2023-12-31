"""CBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from user.views import LoginView
from drf_demo.views import StudentView, StudentDetailView, PublishView, \
    PublishDetailView, AuthorViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('student/', StudentView.as_view()),
    re_path('student/(\d)+/', StudentDetailView.as_view()),
    path('publish/', PublishView.as_view()),
    re_path('publish/(\d)+/', PublishDetailView.as_view()),
    path('author/', AuthorViewSet.as_view()),
    re_path('author/(\d)+/', AuthorViewSet.as_view()),
]


