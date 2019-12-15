from django.urls import path
from orderapp import views
urlpatterns = [
    path('order/', views.OrderView.as_view()),
    path('orderdetails/',views.OrderDetailsView.as_view()),
]
