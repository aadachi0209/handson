from django.urls import path
from .views import index, fortune

app_name = 'おみくじ'

urlpatterns = [
    path('', index),    
    path('fortune_telling', fortune, name='結果'),    
]
