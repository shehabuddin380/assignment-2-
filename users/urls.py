from django.urls import path
from .views import (
    ProfileView, EditProfileView,
    CustomPasswordChangeView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView
)

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", EditProfileView.as_view(), name="edit-profile"),
    path("profile/change-password/", CustomPasswordChangeView.as_view(), name="change-password"),
    path("profile/reset-password/", CustomPasswordResetView.as_view(), name="reset-password"),
    path("reset/<uidb64>/<token>/", CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
