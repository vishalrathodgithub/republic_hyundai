from django.urls import path
from taxapp import views
urlpatterns = [
    path('taxmaster/', views.TaxMasterView.as_view()),
    path('financialyear/',views.FinancialYearView.as_view()),
]
