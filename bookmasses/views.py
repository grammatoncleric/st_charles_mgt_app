from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Bookmass
from django.contrib import messages

# Create your views here.
def bookmass(request):
       if request.method == 'POST':
        bap_first_name=request.POST['bap_first_name']
        bap_middle_name=request.POST['bap_middle_name']
        bap_last_name=request.POST['bap_last_name']
        date_of_birth=request.POST['date_of_birth']
        place_of_birth=request.POST['place_of_birth']
        home_town=request.POST['home_town']
        state_origin=request.POST['state_origin']
        adult_mobile_no=request.POST['adult_mobile_no']
        fathers_name=request.POST['fathers_name']
        fathers_mobile_no=request.POST['fathers_mobile_no']
        mothers_name=request.POST['mothers_name']
        mothers_mobile_no=request.POST['mothers_mobile_no']
        parents_address=request.POST['parents_address']
        parents_marital_status=request.POST['parents_marital_status']
        parents_marriage_parish=request.POST['parents_marriage_parish']
        god_fathers_name=request.POST['god_fathers_name']
        god_fathers_mobile_no=request.POST['god_fathers_mobile_no']
        god_fathers_address=request.POST['god_fathers_address']
        god_mothers_name=request.POST['god_mothers_name']
        god_mothers_mobile_no=request.POST['god_mothers_mobile_no']
        god_mothers_address=request.POST['god_mothers_address']
        user_id=request.POST['user_id'] 

        digital_signature = request.FILES['digital_signature']
        fs = FileSystemStorage()
        name = fs.save(digital_signature.name, digital_signature)
        url = fs.url(name)

        baptism = Baptism(
        bap_first_name =bap_first_name,
        bap_middle_name=bap_middle_name,
        bap_last_name=bap_last_name,
        date_of_birth=date_of_birth,
        place_of_birth=place_of_birth,
        home_town=home_town,
        state_origin=state_origin,
        adult_mobile_no=adult_mobile_no,
        fathers_name=fathers_name,
        fathers_mobile_no=fathers_mobile_no,
        mothers_name=mothers_name,
        mothers_mobile_no=mothers_mobile_no,
        parents_address=parents_address,
        parents_marital_status=parents_marital_status,
        parents_marriage_parish=parents_marriage_parish,
        god_fathers_name=god_fathers_name,
        god_fathers_mobile_no=god_fathers_mobile_no,
        god_fathers_address=god_fathers_address,
        god_mothers_name=god_mothers_name,
        god_mothers_mobile_no=god_mothers_mobile_no,
        god_mothers_address=god_mothers_address,
        digital_signature=digital_signature.name,
        user_id=user_id)
        baptism.save()

        messages.success(request, 'Your baptism request has been submitted, the parish office will get back to you soon. Thank you.')

     

       return render(request, 'pages/bookmass.html')