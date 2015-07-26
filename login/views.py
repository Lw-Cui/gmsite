from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from login.models import UserProfile, AttendLog
import datetime
import json
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

@csrf_exempt
def clockIn(request):
    if request.user.is_authenticated():
        try:
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user = UserProfile.objects.create(user=request.user)
        try:
            log = user.attendlog_set.get(date=datetime.date.today())
        except AttendLog.DoesNotExist:
            log = AttendLog.objects.create(user=user, date=datetime.date.today())
        period = request.POST.get('period', '')
        if log[period] is None:
            log[period] = datetime.datetime.now().time()
            log.save()
        return HttpResponse(json.dumps({
            "date": str(log.date),
            "morning": str(log.morning),
            "afternoon": str(log.afternoon),
            "evening": str(log.evening),
        }))
