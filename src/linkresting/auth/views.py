from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from forms import SignupForm

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

        if(u is None):
            return render(request, 'auth/auth.html', view_data)

        # proceed with creating user
    
    return render(request, 'auth/auth.html')
    
	
def signout(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse("stories.index"))

 		
