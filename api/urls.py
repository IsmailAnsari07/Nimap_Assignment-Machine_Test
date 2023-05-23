from django.urls import path
from api.views import ClientCreateView,ClientDetailView,ProjectCreateView,ClientProjectsDetailView,ProjectListView,UserListView


urlpatterns = [
    path('api/clients/', ClientCreateView.as_view(), name='client-list-create'),
    path('api/clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('api/clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/clients/<int:pk>/projects/', ClientProjectsDetailView.as_view(), name='client-projects-detail'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    
  ] 