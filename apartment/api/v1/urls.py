from django.conf.urls import url
from django.contrib import admin

from .views import (
    ApartmentListAPIView,
    ApartmentDetailAPIView
)

urlpatterns = [
    url(r'^$', ApartmentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ApartmentDetailAPIView.as_view(), name='detail'),

]
