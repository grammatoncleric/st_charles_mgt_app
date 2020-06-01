from django.shortcuts import render, redirect
from .models import Enquiry
from django.contrib import messages
 
def enquiry(request):

        if request.method == 'POST':
          name=request.POST['name']
          email=request.POST['email']
          phone=request.POST['phone']
          message=request.POST['message']         
          user_id=request.POST['user_id']

          contact = Enquiry(name=name, email=email, phone=phone, message=message, user_id=user_id)
          contact.save()

          messages.success(request, 'Your enquiry has been submitted, the parish office will get back to you soon. Thank you.')


        return render(request, 'pages/enquiry.html')
