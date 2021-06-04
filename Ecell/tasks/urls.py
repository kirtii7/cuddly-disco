from django.urls import path
from . import views
app_name = "tasks"
urlpatterns = [
	path("", views.index, name="index"),
	path("status", views.Status, name="Status"),
	path("clear", views.Clearall, name="Clearall"),
	path("delete", views.Delete, name="Delete")
]
