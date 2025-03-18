from django.urls import path
from .views import login_view, signup, logout_view
from . import views
from django.contrib.auth.views import LoginView



urlpatterns=[
        path("login/", login_view, name="login"),
        path("", login_view, name="home"),  # Default route redirects to login
        path('signup/', views.signup, name='signup'),
        path("logout/", logout_view, name="logout"),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('travel/', views.travel, name='travel'),

        
]