from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    # path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('organizer-dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('activate/<uidb64>/<token>/', views.activate_user, name='activate_user'),

]
