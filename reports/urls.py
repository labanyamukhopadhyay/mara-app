from django.urls import path
from . import views

urlpatterns = [
    path("", views.report_index, name="report_index"),
    path("<int:pk>/", views.report_detail, name="report_detail"),
]

