from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="todo"

urlpatterns=[

    url(r"^$", views.IndexView, name="index"),
    url(r'^(?P<id>[0-9]+)/$', views.DetailToDo, name="detail"),
    url(r"^add/$", views.AddTodo, name="create"),
    url(r"^search/$", views.SearchTodo, name="search"),
    url(r'^(?P<id>[0-9]+)/done/$', views.TodoDone, name="done"),
    url(r"^profile/$", views.ProfileView, name="profile"),
    url(r"^search/$", views.SearchTodo, name="search"),

]