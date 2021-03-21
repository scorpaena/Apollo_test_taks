from django.urls import path
from .views import Login, logout_view

urlpatterns = [
    path('login', Login.as_view()),
    path('logout', logout_view),
]
