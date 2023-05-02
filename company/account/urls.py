from django.urls import path
from .views import *

urlpatterns = [
    path('login', Login.as_view(), name='lg'),
    path('addition', Add.as_view(), name='add'),
    path('num_of_words', Count_word.as_view(), name='numw'),
    path('calculator', Calculator.as_view(), name='cal'),
    path('registration', Registration.as_view(), name='reg'),
    path('log_in', Login_form.as_view(), name='log'),
    path('emp_details', Emp_details.as_view(), name='emp_data'),
    path('demp/<int:eid>', Emp_delete.as_view(), name="demp"),

]