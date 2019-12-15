from django.urls import path
from servicesapp import views
urlpatterns = [
    path('labourdetails/', views.LabourDetailsView.as_view()),
    path('labouroperationmaster/',views.LabourOperationMasterView.as_view()),
    path('rodetails/', views.RoDetailsView.as_view()),
    path('ropartdetails/',views.RoPartDetailsView.as_view()),
]
