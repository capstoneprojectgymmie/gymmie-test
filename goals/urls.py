from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exercise/(?P<exercise_id>.*)/$', views.exercise, name='exercise'),
    url(r'^meet_the_team$', views.meettheteam, name='meettheteam'),
    url(r'^progress_report$', views.progressreport, name='progressreport'),
] 
#.* syntax takes all possible strings
urlpatterns += staticfiles_urlpatterns()