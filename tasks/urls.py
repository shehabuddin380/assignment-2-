from django.urls import path
from . import views

urlpatterns = [
    # Home page: Event List
    path('', views.event_list, name='event_list'),

    # Event CRUD
    path('create/', views.event_create, name='event_create'),
    path('edit/<int:pk>/', views.event_update, name='event_edit'),
    path('delete/<int:pk>/', views.event_delete, name='event_delete'),

    # Category CRUD
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_update, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Participant CRUD
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/create/', views.participant_create, name='participant_create'),
    path('participants/edit/<int:pk>/', views.participant_update, name='participant_edit'),
    path('participants/delete/<int:pk>/', views.participant_delete, name='participant_delete'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Search
    path('search/', views.event_search, name='event_search'),

    # RSVP
    path('rsvp/<int:event_id>/', views.rsvp_event, name='rsvp_event'),

    # Optional: If you have a home view, define it on a different route
    # path('home/', views.home, name='home'),  # Not using as homepage now
]
