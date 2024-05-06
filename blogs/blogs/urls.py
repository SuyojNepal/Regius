from django.contrib import admin
from django.urls import path, re_path

from boards import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    path(r'', views.home, name='home'),
]