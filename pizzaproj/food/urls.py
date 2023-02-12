from django.urls import path
from .views import hi , model_test

urlpatterns = [
    path('', model_test, name="test"),
]
