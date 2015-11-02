from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = "<html><body>You do NOT need gas station any longer!</body></html>"
    return HttpResponse(html)
