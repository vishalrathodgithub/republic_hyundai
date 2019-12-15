from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path("signup/",views.signup),
    # path('login1/',auth_views.LoginView.as_view(template_name='loginapp/login.html')),
    # path('password_reset/',auth_views.PasswordResetView.as_view(template_name="loginapp/passreset.html")),
]
