from django.urls import path
from .views import CreateUserView, UserLoginView

urlpatterns = [
    path('register', CreateUserView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name="login")
]