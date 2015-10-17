from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), 
	url(r'^category/(?P<category>\w+)$', views.post_list_category, name='post_list_category'),
]

