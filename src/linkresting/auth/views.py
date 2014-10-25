from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from forms import SignupForm
import string, random, datetime, time


def auth(request):

    return render(request, 'auth/auth.html', {'SignupForm': SignupForm()})

def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('stories.index'))
        else:
            data = {'signin_form': {'errors': True}}
            return render(request, 'auth/auth.html', data)

    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("stories.index"))
    else:
        return render(request, 'auth/auth.html', {'next': request.GET.get('next', '') })

def signup(request):
    # need to check if the user is already logged in
    if request.POST:
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)

        view_data = {
            'request' : request
        }

        # check for required fields
        if(not name or not email or not password1 or not password2):
            view_data.setdefault('signup_form',{}).setdefault('errors',[]).append("Fields marked * are required")
            return render(request, 'auth/auth.html', view_data)

        # validaity checks
        if "@" not in email:
            view_data.setdefault('signup_form',{}).setdefault('errors',[]).append("Invalid email")

        if password1 != password2:
            view_data.setdefault('signup_form',{}).setdefault('errors',[]).append("Confirm password doesn't match")

        if(len(view_data.setdefault('signup_form',{}).setdefault('errors',[])) > 0):
            return render(request, 'auth/auth.html', view_data)
            

        # check if email already exists
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            u = None

        if(u is not None):
            view_data.setdefault('signup_form',{}).setdefault('errors',[]).append("Email address already exists")
            return render(request, 'auth/auth.html', view_data)
        else:
            username = str(int(time.time())) + id_generator(6)
            names = name.split(" ", 1)
            first_name = str(names[0])
            last_name = str(names[1])
            new_user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
            new_user.save()
            if new_user.is_active:
                authenticated_user = authenticate(username=username, password=password1) #need to do this to set the backend property
                login(request, authenticated_user)
                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('stories.index'))

    return render(request, 'auth/auth.html')
    
	
def signout(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse("stories.index"))

 		
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))