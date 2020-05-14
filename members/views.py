from django.shortcuts import render

# Create your views here.
def member(request):
    return render(request, 'pages/member.html')

    