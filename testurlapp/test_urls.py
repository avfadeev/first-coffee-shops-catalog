from testurlapp import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('user/<str:month>/<str:year>/', views.home, name='home'),
]
