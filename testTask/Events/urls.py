from django.urls import path
from .views import Events_list, EventType_list

urlpatterns = [
    path('', Events_list.as_view()),
    path('type', EventType_list.as_view()),
]
