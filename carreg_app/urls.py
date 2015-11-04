from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.UserRegisteration.as_view(), name='user_register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
