from django.urls import path
from . import views # blog 애플리케이션에서 사용할 모든 views를 가져옴


urlpatterns = [
    path('', views.post_list, name='post_list'),
]