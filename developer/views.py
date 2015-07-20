from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from forms import dev_info
from models import developer, attendLog
import datetime

def present():
    now = datetime.datetime.now()
    if now.hour <= 12:
        return 'morning'
    elif now.hour <= 18:
        return 'afternoon'
    else:
        return 'evening'

def status(str = ''):
    is_able = {'morning': 'disabled', 'afternoon': 'disabled', 'evening': 'disabled'}
    if str:
        is_able[str] = ''
    return is_able

def clock_in(request, name, button):
    dev = developer.objects.get(name=name)
    try:
        log = dev.attendlog_set.get(date=datetime.date.today())
    except attendLog.DoesNotExist:
        attendLog.objects.create(date=datetime.date.today(), person=dev)
        log = dev.attendlog_set.get(date=datetime.date.today())
    now = datetime.datetime.now().time()
    if button == 'morning':
        log.morning = now
    elif button == 'afternoon':
        log.afternoon = now
    else:
        log.evening = now
    log.save()

def profile(request, name):
    time_status = status(present())
    if request.method == 'POST':
        button = request.POST.get('now', '')
        if time_status[button] == '':
            clock_in(request, name, button)
            time_status[button] = 'disabled'
    info = {
        'name': name,
        'time':present(),
        'status': time_status,
        'logs': developer.objects.get(name=name).attendlog_set.all(),
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
