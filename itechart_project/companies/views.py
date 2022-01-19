from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render

# Create your views here.
def main_page(request):
    return HTTPResponse('<h1>hello</h1>')
