from django.urls import path
from customerapp import views
urlpatterns = [
    path('state/', views.StateView.as_view()),
    path('district/',views.DistrictView.as_view()),
    path('city/',views.CityView.as_view()),
    path('customerdetails/',views.CustomerDetailsView.as_view()),
    path('existingcustomer/',views.ExistingCustomer.as_view()),

]
