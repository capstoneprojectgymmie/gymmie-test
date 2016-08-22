from django.conf.urls import url
from rango import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update_weight/$', views.update_weight, name="update_weight"),
    url(r'^view_weight/$',views.show_weight, name="view_weight"),
    url(r'^register/$',views.register, name="register"),
    url(r'^login/$',views.user_login, name="login"),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^meet_the_team/$',views.meet_the_team,name='meet_the_team'),
    url(r'^add/(?P<exercise_id>.*)/$', views.add_to_exlog, name='add'),
    url(r'^delete/(?P<routine_id>.*)/$', views.delete_exlog, name='remove'),
]
urlpatterns += staticfiles_urlpatterns()
