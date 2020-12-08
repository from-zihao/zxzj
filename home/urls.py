from django.conf.urls import url

from .views import *


def home_urls():
    urlpatterns = [
        url(r'^api/zxzj/v1/home/image$', HomeView.as_view()),
    ]
    return urlpatterns
