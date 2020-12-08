from django.conf.urls import url

from .views import *


def about_urls():
    urlpatterns = [
        url(r'^api/zxzj/v1/about/info$', AboutView.as_view()),
    ]
    return urlpatterns
