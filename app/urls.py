from django.urls import path
from app import views
app_name="app"

urlpatterns = [
    path('profile/',views.profile,name="profile"),
    path('login/', views.login, name="login"),
    path('sign_up/', views.sign_up, name="signup"),
]
