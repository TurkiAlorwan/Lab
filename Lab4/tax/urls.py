from django.contrib import admin
from django.urls import path, include

from tax import views

urlpatterns = [
    path("", views.index, name="Index"),path("<int:amount>",views.amount,name="amount"),
    path("taxrate",views.returntaxrate,name='Tax rate')
]
