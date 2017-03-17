from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from organizer import views

router = routers.DefaultRouter()

router.register(r'users', views.UserList)
router.register(r'students', views.StudentList)
router.register(r'schedules', views.ScheduleList)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
