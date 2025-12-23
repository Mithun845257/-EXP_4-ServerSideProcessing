from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.home, name='home'),              # main page
    path('bmi', views.bmi_calculator, name='bmi'),  # BMI page
    path('admin/', admin.site.urls),
]
