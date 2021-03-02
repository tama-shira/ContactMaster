from django.urls import path
from . import views

urlpatterns = [
    path('contactmaster', views.SystemList.as_view(), name='system'),
    path('contactmaster/detail/<system_id>', views.detail, name='detail'),
]