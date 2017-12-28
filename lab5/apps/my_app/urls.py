from django.conf.urls import url
from django.contrib import admin
from lab5.apps.my_app import views
from lab5.apps.my_app.views import OrderView, OrdersView

urlpatterns = [
    url(r'^main/', views.main, name='main_url'),
    url(r'^orders/', OrdersView.as_view(), name='orders_url'),
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url'),
]
