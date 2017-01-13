from django.conf.urls import url
from todolist import views


urlpatterns = [
    url(r'^$', views.list_notes, name='list_notes'),
    url(r'^note/create$', views.create_note, name='create_note'),
    url(r'^note/(?P<slug>[\d]+)/edit/$', views.update_note, name='update_note'),
    url(r'^note/(?P<slug>[\d]+)/delete$', views.delete_note, name='delete_note'),
]
