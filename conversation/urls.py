from django.urls import path

from conversation import views

app_name = "conversation"


urlpatterns = [
    path("", view=views.inbox, name="inbox"),
    path("<int:pk>/", view=views.detail, name="detail"),
    path("new/<int:item_pk>/", view=views.new_conversation, name="new"),
]
