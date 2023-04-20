from django.urls import path
from . import views

urlpatterns = [
    path('jpg-to-base64', views.jpgtobase64, name="jpgtobase64"),
]
