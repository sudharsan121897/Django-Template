from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view,  name='login'),
    path('register/', views.register_user,  name='register'),
    path('logout/', views.logout_view,  name='logout_view'),
]