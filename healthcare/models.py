from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Doctor(models.Model):
	name = models.CharField(max_length=100)
	specialization = models.CharField(max_length=100)

class PatientDoctorMapping(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
