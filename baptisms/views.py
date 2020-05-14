from django.shortcuts import render

# Create your views here.
def baptism(request):
          return render(request, 'pages/baptism.html')