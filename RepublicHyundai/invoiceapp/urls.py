from django.urls import path
from invoiceapp import views
urlpatterns = [
    path('preinvoice/', views.preinvoice),
    path('finalinvoice/<int:ro_id>/', views.finalinvoice),
    path('updateprod/<int:pk>/',views.updateprod),
    path('deleteprod/<int:pk>/',views.deleteprod),
    path("updateprodinfo/<int:pk>/",views.updateprodinfo),
    path("addnewprod/<int:pk>/",views.addnewprod),
    path("print/<int:pk>/",views.print),
    path("printpreinvoice/",views.printpreinvoice)
]
