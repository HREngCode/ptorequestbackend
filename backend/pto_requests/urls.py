from django.urls import path
from pto_requests import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('all/', views.get_all_pto_requests),
    path('supervisor/<int:id>/', views.get_request_by_supervisor_number),
    path('employee/<int:id>/', views.get_request_by_employee_id),
    path('request/<id>/', views.get_request_by_id),
    path('employee_number/<int:id>/', views.get_request_by_employee_number),
    path('new/', views.pto_request_create),
    path('update/<int:pk>/', views.pto_request_detail),
    path('approval/<int:pk>/', views.pto_request_approve),
]