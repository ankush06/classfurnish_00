from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns
admin.autodiscover()

urlpatterns = patterns('',

url(r'^$', 'merchant.views.index'),
)