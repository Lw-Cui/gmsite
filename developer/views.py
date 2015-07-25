from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from forms import dev_info
from models import developer, attendLog
import datetime
import json

def present():
    hour = int(datetime.datetime.now().strftime("%H"))
    if 6 < hour <= 12:
        return 'morning'
    elif 12 < hour <= 18:
        return 'afternoon'
    else:
        return 'evening'

def status(str = ''):
    is_able = {'morning': 'disabled', 'afternoon': 'disabled', 'evening': 'disabled'}
    if str:
        is_able[str] = ''
    return is_able

def clock_able(dev, clock_time):
    try:
        log = dev.attendlog_set.get(date=datetime.date.today())
    except attendLog.DoesNotExist:
        log = attendLog.objects.create(date=datetime.date.today(), person=dev)
    if clock_time == 'morning' and log.morning is None:
        return True
    elif clock_time == 'afternoon' and log.afternoon is None:
        return True
    elif clock_time == 'evening' and log.evening is None:
        return True
    return False

def clock_in(dev, clock_time):
    log = dev.attendlog_set.get(date=datetime.date.today())
    now = datetime.datetime.now().time()
    if clock_time == 'morning':
        log.morning = now
    elif clock_time == 'afternoon':
        log.afternoon = now
    else:
        log.evening = now
    log.save()

def profile(request, dev_name):
    dev = developer.objects.get(name=dev_name)
    if clock_able(dev, present()):
        time_status = status(present())
        if request.method == 'POST' and request.POST.get('now', '') == present():
            clock_in(dev, present())
            time_status = status()
    else:
        time_status = status()
    info = {
        'name': dev_name,
        'time':present(),
        'status': time_status,
        'logs': dev.attendlog_set.all()[0:7],
    }
    return render_to_response('profile.html', RequestContext(request, info))

def log_in(request):
    if request.method == 'POST':
        user = dev_info(request.POST)
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        if user.is_valid() and \
                developer.objects.filter(name__exact=name, password__exact=password):
            return HttpResponseRedirect('/profile/' + str(name))
    info = {'form': dev_info()}
    return render_to_response('log_in.html', RequestContext(request, info))

def attend(request):
    pass
