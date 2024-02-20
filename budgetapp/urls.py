
from django.contrib import admin
from django.urls import path

from budgetapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
]
