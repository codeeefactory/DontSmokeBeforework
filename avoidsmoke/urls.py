from django.urls import path
from . import views

urlpatterns = [
    path("Contents/", views.ContentListCreate.as_view(), name="Content-view-create"),
    path(
        "Contents/<int:pk>/",
        views.ContentRetrieveUpdateDestory.as_view(),
        name="update",
    ),
]
