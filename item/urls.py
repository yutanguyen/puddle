from django.urls import path

from item import views

app_name = "item"

urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", view=views.detail, name="detail"),
    path("<int:pk>/edit/", view=views.edit, name="edit"),
    path("<int:pk>/delete/", view=views.delete, name="delete"),
]
