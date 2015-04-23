from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hospital.views.home', name='home'),

    url(r'^', include('appointments.urls', namespace="appointments")),
    url(r'^admin/', include(admin.site.urls)),
]
