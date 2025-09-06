from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import RegisterSerializer, PatientSerializer, DoctorSerializer, MappingSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import serializers

# Registration View
class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = [permissions.AllowAny]

# Patient Views
class PatientListCreateView(generics.ListCreateAPIView):
	serializer_class = PatientSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return Patient.objects.filter(created_by=self.request.user)

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PatientSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return Patient.objects.filter(created_by=self.request.user)

# ---------- Template Views for Patients ----------


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	permission_classes = [permissions.IsAuthenticated]

# Mapping Views
class MappingListCreateView(generics.ListCreateAPIView):
	queryset = PatientDoctorMapping.objects.all()
	serializer_class = MappingSerializer
	permission_classes = [permissions.IsAuthenticated]

class MappingDetailView(generics.RetrieveDestroyAPIView):
	queryset = PatientDoctorMapping.objects.all()
	serializer_class = MappingSerializer
	permission_classes = [permissions.IsAuthenticated]

class PatientMappingsView(generics.ListAPIView):
	serializer_class = MappingSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		patient_id = self.kwargs['patient_id']
		return PatientDoctorMapping.objects.filter(patient_id=patient_id)

class LoginView(generics.GenericAPIView):
	serializer_class = LoginSerializer
	permission_classes = [permissions.AllowAny]

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, _ = Token.objects.get_or_create(user=user)
		return Response({'token': token.key}, status=status.HTTP_200_OK)

# ---------- Template Views for Doctors ----------
class DoctorListCreateView(generics.ListCreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	permission_classes = [permissions.IsAuthenticated]
	
