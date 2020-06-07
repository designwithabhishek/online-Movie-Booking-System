
from paywix.payu import PAYU
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from booking.models import Layouts
# Import Payu from PAYWIX
payu = PAYU()

# Intiate transaction

def preprocessingform(request):
    return render(request,'payment/book-form.html',{})

def checkout(request):
    # Creating unique Transaction ID(change as per your need)
    hash_object = hashlib.sha256(b'randint(0,20)')
    txnid=hash_object.hexdigest()[0:20]
    if request.POST:
       name=request.POST['firstname']
       final_amount=request.POST['amount']
       email=request.POST['email']
       phone=request.POST['phone']
       movie=request.POST['Movie']
       seat=request.POST['seatnumber']
       format=request.POST['format']
       audi=request.POST['audi']
       layout=request.POST['layout']
    payment_data = {
        'txnid': txnid,
        'amount': final_amount,
        'firstname': name,
        'email': email,
        'phone': phone,
        'productinfo': 'trst',
        'udf1':movie,
        'udf2':seat,
        'udf3':format,
        'udf4':audi,
        'udf5':layout
    }
    # Once you make your Dict, Initiate with PAYU
    payu_data = payu.initate_transaction(payment_data)

    # The payu_data contains the input data for the pay payment data
    return render(request, 'payment/checkout.html', {"posted": payu_data})


@csrf_protect
@csrf_exempt
def payment_success(request):
   # Payu will return response success data with hash value
   # Need to verify the data with payu check_hash

   payu_success_data = payu.check_hash(dict(request.POST))
   lid = (payu_success_data['data']['udf5'])
   seats =list(payu_success_data['data']['udf2'].split(","))
   active_layout = Layouts.objects.filter(layout_no=lid)
   for seat in seats:
      a=active_layout.get(seat_number=int(seat))
      a.status=True
      a.save()

   # The payu_success_data return the response data from the payu
	# The hash value is correct or not, with this validation we can find out the
	# whether the response is correct or not

	# Here I just dump the response, Here you have to do your calculations with the data
    #lid = dict(request.POST)['data']['udf5']

    #seats =list(payu_success_data['data']['udf2'].split(","))
    #active_layout = Layouts.objects.filter(layout_no=lid)
    #for seat in seats:
     #   active_layout.get(seat_number=int(seat)).update(status=True)

   return JsonResponse(payu_success_data)

# Failure URL
@csrf_protect
@csrf_exempt
def payment_failure(request):
	# Payu will return response success data with hash value
   # Need to verify the data with payu check_hash


	payu_failure_data = payu.check_hash(dict(request.POST))
	# The payu_failure_data return the response data from the payu
	# The hash value is correct or not, with this validation we can find out the
	# whether the response is correct or not

	# Here I just dump the response, Here you have to do your calculations with the data
	return JsonResponse(payu_failure_data)