from django.urls import path
from dashboardapp import views
# from django.contrib.auth import views as auth_view
urlpatterns = [
    path("dashboard/",views.dashboardview),
    # path("login/",auth_view.LoginView.as_view(template_name="dashboardapp/login.html")),

]
