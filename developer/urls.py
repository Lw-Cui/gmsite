from  django.conf.urls import url, patterns
from views import profile

urlpatterns = patterns(
    'developer.views',
    url(r'^profile/(?P<dev_name>\w+)/', 'profile'),
)