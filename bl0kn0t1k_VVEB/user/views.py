from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse 

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def log_in(request):

    c = {}

    if request.method == 'POST':

        u = authenticate(

            username = request.POST.get('u'),
            password = request.POST.get('p'),

        )

        if u:

            login(request, u)
            return redirect('/home/')

        else: 

            return render(request, 'auth/login.html', {'e': True})

    return render(request, 'auth/login.html')

def register(request):

    if request.method == 'POST':

        name = request.POST.get('n')

        username = request.POST.get('u')
        password = request.POST.get('p')

        username = User(username = username)
        username.set_password(password)
        username.save()

        username.profile.name = name
        username.profile.initials = ''.join(letter[0].upper() for letter in name.split(' '))[0:3]
        username.profile.save()

        username = authenticate(username = username, password = password)
        login(request, username)

        return redirect('/home/')

    return render(request, 'auth/register.html')

def ce(request):

    e = request.POST.get('e')

    if User.objects.filter(username = e).exists():

        return JsonResponse({'u': 'n'})

    else:

        return JsonResponse({'u': 'y'})

def toggle_mode(request):

    request.user.profile.dark_mode = not request.user.profile.dark_mode
    request.user.profile.save()
    return HttpResponse('K')
