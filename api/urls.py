from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('orders/',views.show_orders,name='orders'),
    path('payments/',views.show_payments,name='payments'),
    path('make-order/',views.createOrder,name='make-order'),
    path('item/<uuid:id>/',views.menu_item,name='menu-item'),
    path('order-delete/<uuid:id>',views.delete_order,name='order-delete'),
    ]