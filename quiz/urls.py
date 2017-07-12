from django.conf.urls import url 
from . import views

app_name='quiz'

urlpatterns=[
    url(r'^intro/$',views.intro,name='intro'),
url(r'^(?P<request_id>[0-9]+)/questions/$', views.compete, name='compete'),
url(r'^(?P<request_id>[0-9]+)/move/$', views.move, name='move'),
url(r'^score/$',views.score,name='score'),
url(r'^scoreboard/$',views.scoreboard,name='scoreboard'),
]