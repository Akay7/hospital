from django.conf.urls import url
from .views import AppointmentsFormView, GetFreeTimeView

urlpatterns = [
    url(r'^$', AppointmentsFormView.as_view(), name='registration'),
    url(r'^get_free_time$', GetFreeTimeView.as_view(), name="free_time"),
]