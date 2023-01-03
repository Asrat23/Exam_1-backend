from django.contrib import admin
from django.urls import path
from back_end import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('studlist/', views.student_list.as_view()),
    path('studupdate/<int:pk>', views.student_update.as_view()),
]
