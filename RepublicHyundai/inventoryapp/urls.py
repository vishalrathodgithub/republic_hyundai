from django.urls import path
from inventoryapp import views
urlpatterns = [
    path('productmaster/', views.ProductMasterView.as_view()),
    path('vendordetails/',views.VendorDetailsView.as_view()),
    path('productinventory/',views.ProductInventoryView.as_view()),
]
