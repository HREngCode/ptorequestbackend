from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.employee_list),
    path('<int:pk>/', views.employee_detail),
    path('user/<user>/', views.get_name_by_user_id),
    path('supervisor/<int:id>/', views.get_name_by_supervisor_number),
    path('employee/<int:id>/', views.get_by_employee_param),
    path('pto_balance/<int:pk>/', views.employee_update_pto_balance),
    path('changes/', views.employee_create),
    path('employee_number/<user>/', views.get_name_by_employee_number),
]
