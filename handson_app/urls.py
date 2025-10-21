from django.urls import path
from . import views

app_name = 'handson_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_list', views.PostListView.as_view(), name='post_list'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
]
