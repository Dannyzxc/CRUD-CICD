from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderFormView, name='order_url'),
    path('orders/', views.showView, name='show_url'),
    path('edit/<int:f_oid>', views.updateView, name= 'update_url'),
    path('delete/<int:f_oid>', views.deleteView, name= 'delete_url'),
]