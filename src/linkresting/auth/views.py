from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def auth(request):
	return render(request, 'auth/auth.html')

def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        if '@' in username:
            try:
                check = User.objects.get(email=username)
                username = check.username
            except:
                pass
    
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.POST['next']:
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('/'))
    
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        return render(request, 'auth/auth.html')


def signup(request):
	if request.POST:
		pass
	else:
		HttpResponseRedirect(request, 'auth/auth.html')
 		
