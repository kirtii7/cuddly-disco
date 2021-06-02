from django.urls import path
from . import views
app_name = "Register"
urlpatterns = [
	path("login", views.index, name="index"),
	path("register", views.register, name="register")
]
