from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def signin(request):
    print request.GET.get('next', False)

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
            print "inside error handler"
            data = {
                'forms': {'errors': True}
            }
            return render(request, 'auth/auth.html', data)

    
    if request.user.is_authenticated():
        return HttpResponseRedirect("stories.index")
    else:
        return render(request, 'auth/auth.html', {'next': request.GET.get('next', '') })

def signup(request):
	if request.POST:
		pass
	else:
		HttpResponseRedirect(request, 'auth/auth.html')

def signout(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse("stories.index"))

 		
