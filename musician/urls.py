from django.urls import path
from .views import manage_list, manage_detail

app_name = "musician"

urlpatterns = [
    path("manage/", manage_list, name="manage-list"),
    path("manage/<int:pk>/", manage_detail, name="manage-detail"),
]
