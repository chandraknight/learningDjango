from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request->response
#request habdler
def say_hello(request):
    return HttpResponse("hello this is my first Django Http response")
def render_html_file(request):
    return render(request,'hello.html')
def render_html_file_with_context(request):
    return render(request,'hello.html',context={'name':'chandra'})