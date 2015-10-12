from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^post/$', views.PostViewList.as_view()),
    url(r'^post/(?P<id>\d+)/$', views.PostViewDetail.as_view()),
    url(r'^comment/$', views.CommentViewList.as_view()),
    url(r'^comment/(?P<id>\d+)/$', views.CommentViewDetail.as_view()),
    url(r'^post/(?P<id>\d+)/comment', views.PostComment.as_view()),
]
