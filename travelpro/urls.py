from . import views
from django.urls import path

urlpatterns = [
    path('', views.fun, name='fun'),
    path('add1',views.addition,name='add')
]
