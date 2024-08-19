from django.urls import path
from . import views

urlpatterns = [
    path('',views.dontsmokeview),
    path('CM/',views.comment),
    path('Call/', views.Call),
    path('About/', views.About),
    # path("Contents/", views.ContentListCreate.as_view(), name="Content-view-create"),
    # path(
    #     "Contents/<int:pk>/",
    #     views.ContentRetrieveUpdateDestory.as_view(),
    #     name="update",
    # ),
]
