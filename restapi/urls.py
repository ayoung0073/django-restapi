"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import restapi_app.serializers

app_name='restapi_app'

router = routers.DefaultRouter()
router.register('users', restapi_app.serializers.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls), # 'admin'과 같음
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/v1/', include((router.urls, 'restapi_app'), namespace='api')),
]
