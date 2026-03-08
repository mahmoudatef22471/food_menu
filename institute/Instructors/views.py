from django.http import HttpResponse

def home(request):
    return HttpResponse("Instructors Home Page")