from django.db import models

# Create your models here.  

class Alumnos(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField(max_length=256)
    telefono=models.IntegerField()
    vigencia=models.BooleanField(Default=True)

class Profesores(models.Model):
    nombre=models.CharField(max_length=30)
    rut=models.IntegerField()
    telefono=models.IntegerField()

class Autos(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    patente=models.CharField(max_length=30)

class Horario(models.Model):
    tipoHorario=models.CharField(max_length=10)


class bloqueHorario(models.Model):
    horaInicio=models.CharField(max_length=5)
    horaTermino=models.CharField(max_length=5)
    fecha=models.DateField()
    disponibilidad=models.BooleanField(Default=True)

class Clases_Teoricas(models.Model):
    tema_clase=models.CharField(max_length=30)


class Clases_Practicas(models.Model):
    tema_clase=models.CharField(max_length=30)



 
