from django.urls import path

from server.apps.auth.views import LoginView, LogoutView, RefreshView, StaffLoginView, VerifyView

app_name = "auth"

urlpatterns = [
    path(f"{app_name}/login/", LoginView.as_view(), name="login"),
    path(f"{app_name}/logout/", LogoutView.as_view(), name="logout"),
    path(f"{app_name}/token/verify/", VerifyView.as_view(), name="token_verify"),
    path(f"{app_name}/token/refresh/", RefreshView.as_view(), name="token_refresh"),
    path(f"{app_name}/staff/login/", StaffLoginView.as_view(), name="staff_login"),
]
