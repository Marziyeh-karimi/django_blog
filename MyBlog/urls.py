from django.urls import path
from .views import HomeTemp

urlpatterns=[
    path('',HomeTemp.as_view(),name='home'),
]