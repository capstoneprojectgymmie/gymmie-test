#urls python
#.* syntax takes all possible strings
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
    url(r'^user_dashboard$',views.userdashboard, name='userdashboard'),
    url(r'^register$',views.registeruser,name="registeruser"),
    url(r'^abs$', views.abss, name='abs'),
    url(r'^abds$', views.abds, name='abds'),
    url(r'^adds$', views.adds, name='adds'),
    url(r'^bis$', views.bis, name='bis'),
    url(r'^cavs$', views.cavs, name='cavs'),
    url(r'^chst$', views.chst, name='chst'),
    url(r'^farms$', views.farms, name='farms'),
    url(r'^gluts$', views.gluts, name='gluts'),
    url(r'^hams$', views.hams, name='hams'),
    url(r'^lats$', views.lats, name='lats'),
    url(r'^lback$', views.lback, name='lback'),
    url(r'^mback$', views.mback, name='mback'),
    url(r'^neck$', views.neck, name='neck'),
    url(r'^quad$', views.quad, name='quad'),
    url(r'^shldr$', views.shldr, name='shldr'),
    url(r'^trap$', views.trap, name='trap'),
    url(r'^tris$', views.tris, name='tris'),
] 
#.* syntax takes all possible strings
urlpatterns += staticfiles_urlpatterns()
