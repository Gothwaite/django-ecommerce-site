"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from products.views import index,product_page,place_order,login_or_create,login_usr,create_usr,create_account,logout_view
from products.models import Products,Orders

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^product_page/(?P<name>[a-zA-Z0-9_.-]+)/$', product_page),
    url(r'^place_order/$', place_order),
    url(r'^login_or_create/$', login_or_create),
    url(r'^login_usr/$', login_usr),
    url(r'^create_usr/$', create_usr),
    url(r'^create_account/$', create_account),
    url(r'^logout/$', logout_view),
 #   url(r'^', index),
   

]
