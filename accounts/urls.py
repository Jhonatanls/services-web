from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Index
    path('', views.dashboard, name='dashboard'),
    # Login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Cambio de contraseña
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Registrar usuarios
    path('register/', views.register, name='register'),
    path('register_done/', views.register, name='register_done')



]