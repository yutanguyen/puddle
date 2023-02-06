from django.contrib.auth import views as auth_views
from django.urls import path

from core import views
from core.forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", view=views.signup, name="signup"),
    path(
        "login/",
        view=auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
]
