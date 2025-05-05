from django.urls import path
from. import views 


app_name = 'seeker'
urlpatterns = [
    path('', views.homepage, name='homepage'),
]