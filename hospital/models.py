from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = encrypt(models.CharField(max_length=40))
    mobile = encrypt(models.CharField(max_length=20, null=True))
    department = encrypt(models.CharField(max_length=50, choices=departments, default='Cardiologist'))
    status = models.BooleanField(default=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = encrypt(models.CharField(max_length=40))
    mobile = encrypt(models.CharField(max_length=20, null=False))
    symptoms = encrypt(models.CharField(max_length=100, null=False))
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = encrypt(models.DateField(auto_now=True))
    status = models.BooleanField(default=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        # return self.user.first_name + " " + self.symptoms
        return "{} ({})".format(self.user.first_name, self.symptoms)


class Appointment(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = encrypt(models.TextField(max_length=500))
    prescription = encrypt(models.TextField(max_length=2000, blank=True))
    status = models.BooleanField(default=True)


