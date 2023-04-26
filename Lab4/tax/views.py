from django.http import HttpResponse
from django.shortcuts import render

tax_rate = 1.15


# Create your views here.
def index(request):
    return render(request, "s.html")


def amount(request, amount):
    return HttpResponse(f'the amount after taxes is: {amount * tax_rate}')


def returntaxrate(request):
    return HttpResponse(f'<h1> The Tax Rate is: {tax_rate} <h1/>')
