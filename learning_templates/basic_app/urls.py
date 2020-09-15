from django.conf.urls import url
from basic_app import views
from django.urls import path

#Template tagging
# SET THE NAMESPACE!
app_name = 'basic_app'

#urlpatterns=[
#    path("", views.relative, name="relative"),
#    path("", views.other, name="other"),
#]

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
