from django.db import models

class Person(models.Model):
    person_ssn = models.IntegerField(primary_key=True)
    person_fname = models.CharField(max_length=20)
    person_lname = models.CharField(max_length=50)
    person_email = models.CharField(max_length=70)
    person_phone = models.IntegerField()
    person_addr = models.CharField(max_length=100)
    person_priority = models.IntegerField()
    person_is_medic = models.BooleanField(default=False)

class Medic(models.Model):
    medic_ssn = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    medic_type = models.CharField(max_length=25)
    medic_was_vaccinated = models.BooleanField(default=False)

class Patient(models.Model):
    patient_ssn = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    patient_wants_vaccine = models.BooleanField(default=False)
    patient_was_vaccinated = models.BooleanField(default=False)

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=25, primary_key=True)
    vaccine_stock = models.IntegerField()
    vaccine_no_of_shots = models.IntegerField()
    vaccine_effectivity = models.FloatField()

class Place(models.Model):
    place_id = models.IntegerField(primary_key=True)
    place_name = models.CharField(max_length=30)
    place_addr = models.CharField(max_length=50)

class PlaceHasVaccines(models.Model):
    stock = models.IntegerField()
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

class Appointment(models.Model):
    shot_no = models.IntegerField()
    appointment_date = models.DateField()
    appointment_next_date = models.DateField()
    appointment_priority = models.IntegerField()
    patient_ssn = models.ForeignKey(Patient,on_delete=models.CASCADE)
    medic_ssn = models.ForeignKey(Medic, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
