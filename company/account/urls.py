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
    path('dlt_emp/<int:eid>', Emp_delete.as_view(), name="demp"),  # int:eid  recives datum.id from template
    path('emp_update/<int:eid>', Emp_update.as_view(), name='update'),
    path('add_manager', Mng_reg.as_view(), name='regm'),
    path('mamagers data', Mng_table.as_view(), name='mng_data'),
    path('dlt_mng/<int:mid>', Mng_delete.as_view(), name="dmng"), 

]