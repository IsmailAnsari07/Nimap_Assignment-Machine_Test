from django.urls import path
from .views import *

urlpatterns=[
    path('create_client/',ClientCreateView.as_view(),name='create_client'),
    path('client_detail/', ClientInfoView.as_view(),name='client_detail'),
    path('update_client/<int:pk>/', UpdateClientView.as_view(),name='update_client'),
    path('delete_client/<int:id>/', DeleteClientView.as_view(),name='delete_client'),

    path('project_create/',ProjectCreateView.as_view(),name='project_create'),
    path('project_list/',AllRecordsFromProjects.as_view(),name='project_list'),
    path('project_detail/',ProjectDetailView.as_view(),name='project_detail'),
]