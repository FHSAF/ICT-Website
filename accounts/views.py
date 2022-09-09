from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from contacts.models import Contact
from accounts import models
import re
# django-email-confirmation


from django.views.decorators.csrf import csrf_exempt

from accounts.forms import EditProfileForm, SignUpForm
from validate_email import validate_email

# verification of account
from django.conf import settings
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.template.loader import get_template


from django_email_verification import send_email


@csrf_exempt
def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        surename = request.POST['surename']
        email = request.POST['email']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        birth_date = request.POST['birth_date']
        password = request.POST['password']
        password2 = request.POST['password2']

        # valid_email = validate_email(email, verify=True)

        # if not valid_email:
        #     messages.error(request, 'email does not exist!')
        #     return redirect('register')
        # Check if passwords match
        if password == password2:
            # Check username
            if not len(password) >= 8:
                messages.error(
                    request, 'password must atleast be 8 charaters long!')
                return redirect('register')
            if not re.findall('[a-z]', password):
                messages.error(request, 'password myset contain lowercase!')
                return redirect('register')
            if not re.findall('[A-Z]', password):
                messages.error(request, 'password myset contain Uppercase!')
                return redirect('register')
            if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
                messages.error(request, 'password myset contain character!')
                return redirect('register')
            if not re.findall('\d', password):
                messages.error(request, 'password myset contain numbers!')
                return redirect('register')
            else:
                if models.UserProfile.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = models.UserProfile.objects.create_user(
                        password=password, email=email, firstname=firstname, lastname=surename, address=address, phone_number=phone_number, birth_date=birth_date)

                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')

                    user.save()
                    # send_email(user)
                    messages.success(
                        request, 'Registration completed, please check your email, activate your account and login!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'Form/register_form.html')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')
    else:
        form = SignUpForm()
    template_name = 'Form/register_form.html'
    return render(request, template_name, {'form': form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        if not user.is_verified:

            messages.error(
                request, 'User profile is not verified, check you email please!')
            return redirect('login')

        auth.login(request, user)
        messages.success(request, 'You are now logged in')
        return redirect('index_view_url')

    else:
        return render(request, 'Form/login_form.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    # user_contacts = Contact.objects.order_by(
    #     '-contact_date').filter(user_id=request.user.id)

    # context = {
    #     'contacts': user_contacts
    # }
    return render(request, 'accounts/dashboard.htm')


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = EditProfileForm(instance=request.user)
        args = {"form": form}
        return render(request, "accounts/edit_profile.htm", args)


# def update_profile(request):
#     args = {}

#     if request.method == 'POST':
#         form = UpdateProfile(request.POST)
#         form.actual_user = request.user
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('update_profile_success'))
#     else:
#         form = UpdateProfile()

#     args['form'] = form
#     return render(request, 'registration/update_profile.htm', args)


# def sendEmail(request):
#     password = request.POST.get('password')
#     password = request.POST.get('password')
#     password = request.POST.get('password')
#     user = get


def send_mail_after_registration(email, token, firstname):
    subject = 'Your account needs to be verified'

    message = get_template("mail_body.html").render(
        {'name': firstname, 'token': token})
    email_from = settings.EMAIL_HOST_USER

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=email_from,
        to=[email]
    )

    mail.content_subtype = "html"
    return mail.send()


def verify(request, auth_token):
    profile_obj = models.UserProfile.objects.filter(
        auth_token=auth_token).first()
    try:
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(
                    request, "Your account has already been verified!")
                return redirect('login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(
                request, "You have successfully verified your account!")
            return redirect('login')

        else:
            return redirect('error')

    except Exception as e:
        print(e)


def error_page(request):
    return render(request, 'partials/error.html')
