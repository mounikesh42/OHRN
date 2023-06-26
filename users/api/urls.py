from django.urls import path
from users.api.views import (
    UserRegistrationView,
    LoginView,
    UserDetailView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', UserRegistrationView.as_view(),name="user-register"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/', UserDetailView.as_view()),

]