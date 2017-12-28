from django.shortcuts import render, HttpResponse
from django.views import View
import random

# Create your views here.


def main(request):
    return render(request, 'main_page.html')


class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'The first order', 'id': 1},
                {'title': 'The second order', 'id': 2},
                {'title': 'The third order', 'id': 3},
            ]
        }
        return render(request, 'orders\orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render (request, 'orders\order.html', data)
