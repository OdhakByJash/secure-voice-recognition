from django.urls import path
from voice_recognition.views import register,verify
urlpatterns = [
    path('register/',register,name='register'),
    path('verify/',verify,name='verify')
]