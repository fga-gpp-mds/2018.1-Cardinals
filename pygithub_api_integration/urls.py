from django.conf.urls import url
from pygithub_api_integration import views

urlpatterns = [
    url(r'getContributors/$', views.getContributors, name='getContributors')
]
