from django.urls import path
from .views import *

urlpatterns = [
    path("studentsHome/", Std.as_view(), name ='std'),
    path("studentRegistration/", Std_Reg.as_view(), name = 'rstd'),
    path("studentUpdate/<int:sid>", Std_Update.as_view(), name='ustd'),
    path("StudentDelete/<int:sid>", Std_Delete.as_view(), name='dstd'),

]