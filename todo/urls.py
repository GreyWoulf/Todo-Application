from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, register

urlpatterns = [
  path("", home, name="home"),
  path("login/", LoginView.as_view(template_name="todo/login.html"), name="login"),
  path("logout/", LogoutView.as_view(template_name="todo/logout.html"), name="logout"),
  path("register/", register, name="register"),
]