from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("version8!-CI/CD Hello, world. You're at the polls index.")

