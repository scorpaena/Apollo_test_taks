from django.urls import path
from .views import EventList, EventTypeList

urlpatterns = [
    path('', EventList.as_view()),
    path('type', EventTypeList.as_view()),
]
