from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/profile/")
    return render_to_response("login.html", RequestContext(request))


def profile(request):
    if request.user.is_authenticated():
        info = {
            "username": request.user.username,
        }
        return render_to_response("profile.html", RequestContext(request, info))
    else:
        return redirect('login.views.login')
