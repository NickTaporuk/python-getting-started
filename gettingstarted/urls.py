from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^apartment/', include('apartment.urls')),
    url(r'^api/v1/apartments/', include('apartment.api.v1.urls', namespace='apartment-api-v1')),
    url(r'^admin/', include(admin.site.urls)),
]
