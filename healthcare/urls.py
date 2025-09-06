from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    
    path('register/', views.RegisterView.as_view(), name='register'),
    



    # Patient APIs
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
  


    # Doctor APIs
 
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
   

    # Patient-Doctor Mapping APIs
    path('mappings/', views.MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', views.MappingDetailView.as_view(), name='mapping-detail'),
  

]