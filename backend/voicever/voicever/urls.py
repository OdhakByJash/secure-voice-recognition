from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('voice-recognition/',include('voice_recognition.urls')),
    path('challenge-response/',include('challengeresponse.urls'))
]