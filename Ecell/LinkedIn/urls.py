from django.urls import path
from . import views
app_name = "LinkedIn"
urlpatterns = [
	path("", views.index, name="index"),
]
