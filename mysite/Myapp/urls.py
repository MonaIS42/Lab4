from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index") ,
    path("<int:num>", views.newprice, name="index") ,
    path("tax_rate", views.taxrate, name="index")

]