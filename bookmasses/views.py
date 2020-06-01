from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Bookmass
from django.contrib import messages

# Create your views here.
def bookmass(request):
       if request.method == 'POST':
        bookmass_time=request.POST['thanksgiving_dayTime']
        category=request.POST['fullname']
        fullname=request.POST['fullname']
        mobile_no=request.POST['mobile_no']
        names_to_pray_for=request.POST['names_to_pray_for']
        intention=request.POST['intention']
        intention_category=request.POST['intention_category']
        intention_start_date =request.POST['intention_start_date']
        intention_end_date =request.POST['intention_end_date']
        amount_paid =request.POST['amount_paid']
        have_open_thanksgiving =request.POST['have_open_thanksgiving']
        thanksgiving_day=request.POST['thanksgiving_day']
        thanksgiving_time=request.POST['thanksgiving_time']
        if not request.user.is_authenticated:
          user_id=0
        else:
          user_id=request.POST['user_id']

         

        photo_pay_evidence = request.FILES['photo_pay_evidence']
        fs = FileSystemStorage()
        name = fs.save(photo_pay_evidence.name, photo_pay_evidence)
        url = fs.url(name)


        bookmass = Bookmass(
              bookmass_time =bookmass_time,
              category =category,
              fullname =fullname,
              mobile_no =mobile_no,
              names_to_pray_for =names_to_pray_for,
              intention =intention,
              intention_category =intention_category,
              intention_start_date =intention_start_date,
              intention_end_date =intention_end_date,
              amount_paid =amount_paid,
              have_open_thanksgiving =have_open_thanksgiving,
              thanksgiving_day =thanksgiving_day,
              thanksgiving_time =thanksgiving_time,
              photo_pay_evidence=photo_pay_evidence.name,
              user_id=user_id)
        bookmass.save()

        messages.success(request, 'Your mass booking request has been submitted, the parish office will get back to you soon. Thank you.')

     

       return render(request, 'pages/bookmass.html')