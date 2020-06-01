from django.shortcuts import render, redirect
from .models import Member
from django.contrib import messages

# Create your views here.
def member(request):
    
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        resident_address=request.POST['residence_address']
        office_address=request.POST['office_address']
        mobile_no=request.POST['mobile_no']
        lga_origin=request.POST['lga_origin']
        state_origin=request.POST['state_origin']
        occupation=request.POST['occupation']
        gender=request.POST['gender']
        date_of_birth=request.POST['date_of_birth']
        marital_status=request.POST['marital_status']
        married_in_catholic=request.POST['married_in_catholic']
        nok_name=request.POST['nok_name']
        nok_phone=request.POST['nok_phone']
        sacraments_received=request.POST['sacrament_received']
        when_you_start_worship=request.POST['when_you_start_worship']
        belong_to_association=request.POST['belong_to_association']
        association_names=request.POST['association_names']
        if not request.user.is_authenticated:
          user_id=0
        else:
          user_id=request.POST['user_id']

        #check if user has already registered
        is_registered = Member.objects.all().filter(first_name=first_name, last_name=last_name)

        if is_registered:
            messages.error(request, 'You have already register at St.Charles Borromeo Parish. Thank you.')
        return render(request, 'pages/member.html')

        member = Member(first_name=first_name,
        last_name=last_name, email=email, resident_address=resident_address, 
        office_address=office_address, mobile_no=mobile_no, lga_origin=lga_origin, 
        state_origin=state_origin, occupation=occupation, gender=gender,
         date_of_birth=date_of_birth, marital_status=marital_status, 
         married_in_catholic=married_in_catholic, nok_name=nok_name, nok_phone=nok_phone,
          sacraments_received=sacraments_received, when_you_start_worship=when_you_start_worship,
           belong_to_association=belong_to_association, association_names=association_names, user_id=user_id)
        member.save()

        messages.success(request, 'Your membership request has been submitted, the parish office will get back to you soon. Thank you.')

    return render(request, 'pages/member.html')

    