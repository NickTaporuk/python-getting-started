from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^apartment/', include('apartment.urls')),
    url(r'^api/v1/apartments/', include('apartment.api.v1.urls', namespace='apartment-api-v1')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/login/', obtain_jwt_token),
    url(r'^api/v1/auth/refresh/', refresh_jwt_token),
    url(r'^api/v1/auth/verify/', verify_jwt_token),
]
