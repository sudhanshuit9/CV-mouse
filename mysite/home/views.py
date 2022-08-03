from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicepage")

def contacts(request):
    return HttpResponse("this is contacstpage")