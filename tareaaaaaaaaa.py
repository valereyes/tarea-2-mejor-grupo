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
    año=models.IntegerField()

class Horario(models.Model):
    tipoHorario=models.CharField(max_length=10)


class bloqueHorario(models.Model):
    horaInicio=models.CharField(max_length=5)
    horaTermino=models.CharField(max_length=5)
    fecha=models.DateField()
    disponibilidad=models.BooleanField(Default=True)

class Clases_Teoricas(models.Model):

class Clases_Practicas(models.Model):


class Grupo(models.Model):
    nombre=models.CharField(max_length=30)
    proyecto=models.OneToOneField(Proyecto,on_delete=models.CASCADE)


class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField(max_length=256)
    numero=models.IntegerField()
    grupo=models.ForeignKey(Grupo,on_delete=models.CASCADE)


class Desafio(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=512)
    fecha=models.DateField()


class DesafiosEstudiantes(models.Model):
    estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    desafio=models.ForeignKey(Desafio,on_delete=models.CASCADE)
    fueEntregado=models.BooleanField(default=False)