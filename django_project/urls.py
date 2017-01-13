from django.conf.urls import url, include
from django.contrib.auth import views
from django.contrib import admin

urlpatterns = [
    url(r'^', include('todolist.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, {'template_name': 'todolist/login.html'}, name='user_login'),
    url(r'^logout/$', views.logout, {'next_page': '/'}, name='user_logout'),
]
