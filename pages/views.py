from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from baptisms.models import Baptism

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def print_baptism(request, id):

    if request.user.is_authenticated:
        user_id=request.user.id
    
        baptism_obj = get_object_or_404(Baptism, pk=id)
        context = {'baptism': baptism_obj}

    return render(request, 'pages/baptism_print.html', context)

