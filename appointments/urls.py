from django.conf.urls import url
from .views import AppointmentsFormView

urlpatterns = [
    url(r'^$', AppointmentsFormView.as_view()),
]