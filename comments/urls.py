from django.conf.urls import url

from comments import views as comment_views
from comments import views as comment_thread


urlpatterns = [
    url(r'^(?P<id>[\d]+)/$', comment_views.comment_thread, name='thread'),
    #url(r'^(?P<slug>[-\w]+)/delete/$', comment_delete, name='delete'),
]