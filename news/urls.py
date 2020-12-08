from django.conf.urls import url

from .views import *


def news_urls():
    urlpatterns = [
        url(r'^api/zxzj/v1/news/record$', NewsView.as_view()),
        url(r'^api/zxzj/v1/news/document$', NewsDocView.as_view()),
    ]
    return urlpatterns
