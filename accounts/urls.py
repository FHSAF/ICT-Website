from django.urls import path, include
from django.contrib import messages

from django.contrib.auth.views import LoginView, LogoutView

from . import views
from django_email_verification import urls as email_url


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path("logout", LogoutView.as_view(next_page='index_view_url'), name="logout"),
    path("edit", views.edit_profile, name="edit"),
    path('dashboard', views.dashboard, name='dashboard'),

    # path('verify/<auth_token>', views.verify, name="verify"),
    # path('error/', views.error_page, name="error")
]
# path('logout', views.logout, name='logout'),
