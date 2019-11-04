from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'allpages/index.html', {'title':'Home'})

def about_view(request):
    return render(request, 'allpages/about.html', {'title':'About Us'})

def privacy_view(request):
    return render(request, 'allpages/privacy.html', {'title':'Privacy Policy'})