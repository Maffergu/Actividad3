from django.db import models

# Create your models here.
class Alumno(models.Model):
    CodAlumno = models.CharField(max_length=100, null=False, blank=False)
    avance = models.IntegerField()

    def __str__(self):
        return f'{self.CodAlumno} - {self.avance}'
