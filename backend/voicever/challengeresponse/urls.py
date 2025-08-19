from django.urls import path
from challengeresponse.views import challenege_view,response_view
urlpatterns = [
    path("challenge/",challenege_view,name="challenge"),
    path("response/",response_view,name="response")
]
