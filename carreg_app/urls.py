from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # POST to this url implies registeration
    url(r'^users/$', views.UserRegisteration.as_view(), name='user_register'),
    url(r'^users/login/$', views.UserLogin.as_view(), name='user_login'),
    url(r'^users/refuel/$', views.UserRefuel.as_view(), name='user_refuel'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
