# users/views.py
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import login
from .forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Password set
            user.is_active = False
            user.save()
            group = Group.objects.get(name='Participant')
            user.groups.add(group)

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = f"http://{domain}/users/activate/{uid}/{token}/"

            subject = "Activate your account"
            message = f"Hi {user.username}, click the link to activate your account: {link}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

            return HttpResponse("Check your email to activate your account.")
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('dashboard_redirect')
    return HttpResponse("Activation link is invalid!")
#organizer checker function
def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()

@login_required
@user_passes_test(is_organizer)
def organizer_dashboard(request):
    return render(request, 'users/organizer_dashboard.html')

