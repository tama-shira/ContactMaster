from django.urls import path
from . import views

urlpatterns = [
    path('', views.SystemList.as_view(), name='system'),
    path('detail/<system_id>', views.detail, name='detail'),
    path('search', views.SearchList.as_view(), name='search'),
]