from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]