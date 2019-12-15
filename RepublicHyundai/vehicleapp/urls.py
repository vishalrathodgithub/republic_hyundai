from django.urls import path
from vehicleapp import views
urlpatterns = [
    path('vehiclemodel/', views.VehicleModelView.as_view()),
    path('vehicledetails/',views.VehicleDetailsView.as_view()),
]
