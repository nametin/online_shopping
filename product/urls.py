from django.urls import  path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("list",views.list, name="list"),
    path("<int:product_id>", views.details, name="details")
]