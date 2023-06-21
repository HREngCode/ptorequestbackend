from django.urls import path, include
from . import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('employee/<id>/', views.comments_list_by_employee),
    path('request/<id>/', views.comments_list_by_request),
    path('update/<pk>/', views.comments_detail),
    path('all/', views.get_all_comments),
    path('changes/', views.user_comments),
]