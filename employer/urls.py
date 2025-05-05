from django.urls import path
from. import views 


app_name = 'professional'
urlpatterns = [
    path('', views.homepage, name='homepage'),
]