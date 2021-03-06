"""zxzj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from news.urls import news_urls
from home.urls import home_urls
from about.urls import about_urls
from case.urls import case_urls
from contact.urls import contact_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

# news urls
urlpatterns += news_urls()

# home urls
urlpatterns += home_urls()

# about urls
urlpatterns += about_urls()

# case urls
urlpatterns += case_urls()

# contact urls
urlpatterns += contact_urls()
