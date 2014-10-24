from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

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
    return render(request, 'auth/auth.html', {SignupForm: SignupForm()})
    
	

def signout(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse("stories.index"))

 		
