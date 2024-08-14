from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name="vlog-home"),
    path('about/', views.about, name="vlog-about"),
]
