from django.conf.urls import url
from . import views

#テンプレートのパス
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
