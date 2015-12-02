from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # POST to this url implies registeration
    url(r'^users/register/', views.UserRegisteration.as_view()),
    url(r'^users/(?P<user_id>[0-9]+)/refuel/$', views.UserRefuel.as_view(),
        name='user_refuel'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
