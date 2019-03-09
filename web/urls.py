
from django.conf.urls import url

from web import views

urlpatterns = [
    # 前台主页
    url(r'index/', views.index, name='index'),
    url(r'view/', views.view, name='view'),
    url(r'comment/', views.comment, name='comment'),
    url(r'article/(\d+)/', views.article, name='article'),

    # url(r'new/', views.new, name='new'),
    # url(r'newlist/', views.newlist, name='newlist'),
    # url(r'about/', views.about, name='about'),
    # url(r'infopic/', views.infopic, name='infopic'),
]