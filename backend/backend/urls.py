from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from organizer import views

router = routers.DefaultRouter()

router.register(r'users', views.UserList)
router.register(r'students', views.StudentList)
router.register(r'schedules', views.ScheduleList)
router.register(r'parents', views.ParentList)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^register', views.RegisterView.as_view(), name='register'),
    url(r'^create_student', views.CreateStudent.as_view(), name='create_student'),
    url(r'^create_schedule', views.CreateSchedule.as_view(), name='create_schedule'),
    url(r'^create_parent', views.CreateParent.as_view(), name='create_parent'),
    url(r'^get_student', views.GetStudent.as_view(), name='get_student'),
    url(r'^get_parent', views.GetParent.as_view(), name='get_parent'),
    url('^get_schedule', views.GetScheduleWithStudentId.as_view(), name='get_schedule'),
]
