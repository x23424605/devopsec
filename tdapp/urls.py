from django.urls import path
from .views import login_view, logout_view
from . import views
from django.contrib.auth.views import LoginView



urlpatterns=[
        path("login/", login_view, name="login"),
        path("", login_view, name="home"),  # Default route redirects to login
        path('signup/', views.signup, name='signup'),
        path("logout/", logout_view, name="logout"),
        path('dashboard/', views.dashboard, name='dashboard'),
        # path('travel/', views.travel, name='travel'),
        path("book/<str:country>/", views.room_booking, name="book_room"),
        path("success/<int:booking_id>/", views.success, name="success"),
        path("myplans/", views.myplans, name="myplans"),
        path('booking/update/<int:id>/', views.updatebooking, name='update'),
        path('booking/delete/<int:id>/', views.deletebooking, name='delete'),
]