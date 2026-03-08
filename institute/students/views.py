from django.http import HttpResponse

def home(request):
    return HttpResponse("Students Home Page")