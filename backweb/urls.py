
from django.conf.urls import url

from backweb import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),
    # 注册
    url(r'^register/', views.register, name='register'),
    # 后台主页
    url(r'^index/', views.index, name='index'),
    # 后台文章页
    url(r'^article/', views.article, name='article'),
    # 后台添加文章页
    url(r'^add_article/', views.add_article, name='add_article'),
    # 后台更新文章页
    url(r'^update_article/(\d+)/', views.update_article, name='update_article'),
    # 后台删除文章页
    url(r'^del_article/(\d+)/', views.del_article, name='del_article'),
    # 后台栏目
    url(r'^category/', views.category, name='category'),
]