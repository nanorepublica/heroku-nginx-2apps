from django.http import HttpResponse

# Create your views here.


def index(request, *args, **kwargs):
    return HttpResponse('WORLD')
