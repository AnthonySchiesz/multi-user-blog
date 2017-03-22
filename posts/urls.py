from django.conf.urls import url
from django.contrib import admin

from posts import views as post_views
from posts import views as post_list
from posts import views as post_create
from posts import views as post_detail
from posts import views as post_update
from posts import views as post_delete
from posts import views as like_post
from .views import PostLikeToggle, PostLikeAPIToggle

urlpatterns = [
	url(r'^$', post_views.list, name='list'),
	url(r'^create/$', post_views.create, name='create'),
	url(r'^(?P<slug>[-\w]+)/$', post_views.detail, name='detail'),
	url(r'^(?P<slug>[-\w]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
	url(r'^api/(?P<slug>[-\w]+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
	url(r'^(?P<slug>[-\w]+)/edit/$', post_views.update, name='update'),
	url(r'^(?P<slug>[-\w]+)/delete/$', post_views.delete, name='delete'),
]
