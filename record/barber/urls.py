from django.urls import path, re_path
from . import views


urlpatterns = [
    
    path('', views.barber_count, name='barber'),
    path('<int:month>/<int:num>/<int:year>', views.barber_count, name='count'),
    path('price/', views.price, name='price'),
]