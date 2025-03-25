
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('',views.home,name='home'),
    path('login/',views.log_in, name='login'),
]
