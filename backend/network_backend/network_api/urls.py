from django.urls import path
from .views import PersonAPIView

urlpatterns = [
    path('person/', PersonAPIView.as_view()),
]
