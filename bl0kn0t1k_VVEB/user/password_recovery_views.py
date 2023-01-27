from django.shortcuts import render, HttpResponse, get_object_or_404

from django.core.mail import send_mail
from django.conf import settings
from uuid import uuid4

from django.contrib.auth.models import User
from .models import Profile

def forgot_password(request):

    return render(request, 'auth/forgot-password.html')

def send_recovery_email(request):

    email = request.POST.get('e')

    try:
        user = User.objects.get(username = email)

        token = uuid4()

        user.profile.password_recovery_token = token
        user.profile.save()

        subject = 'Восстановление пароля от вашего Блокнотика'
        message = f'https://bloknot-ik.ru/reset-password/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.username]
        send_mail(subject, message, email_from, recipient_list)

        return HttpResponse('K')

    except:
        return HttpResponse('N')

def reset_password(request, password_recovery_token):

    profile = get_object_or_404(Profile, password_recovery_token = password_recovery_token)

    return render(request, 'auth/reset-password.html', {'user': profile})
    