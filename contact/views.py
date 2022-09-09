from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    birth_date = request.POST['birth_date']
    subject = request.POST['subject']
    message = request.POST['message']
    user_id = request.POST['user_id']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      # has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      # if has_contacted:
      #   messages.error(request, 'You have already made an inquiry for this listing')
      #   return redirect('/listings/'+listing_id)

    contact = Contact(name=name, email=email, phone_number=phone_number, message=message, subject=subject, birth_date=birth_date, user_id=user_id )

    contact.save()

    # # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + subject + '. Sign into the admin panel for more info',
    #   'fedasameh2018@gmail.com',
    #   ['sam.gug2020@gmail.com', 'fedasameh2015@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/')
