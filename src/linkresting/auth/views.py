from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def auth(request):
	return render(request, 'auth/auth.html')

def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.POST.get('next', False):
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('stories.index'))
    
    if request.user.is_authenticated():
        return HttpResponseRedirect("stories.index")
    else:
        return render(request, 'auth/auth.html')

def signup(request):
	if request.POST:
		pass
	else:
		HttpResponseRedirect(request, 'auth/auth.html')

def signout(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse("stories.index"))

 		
