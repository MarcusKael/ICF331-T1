from django.db import models

class Curso(models.Model):
    sigla=models.CharField(max_length=6)
    nombre=models.CharField(max_length=60)
    creditos=models.IntegerField()
    cursos=models.Manager()

    def __str__(self):
                 return "{}".format(self.nombre)
                    
class CursoFactory:
    def __init__(self):
                 self.cursos = []
                 self.cursos.append(Curso("ICF232","Ingenieria de Software I",6))
                 self.cursos.append(Curso("ICF121","Introduccion a la Ingenieria Civil Informatica",6))
                
    def obtenerCursos(self):
                 return self.cursos

    def getCurso(self,sigla):
        for curso in self.cursos:
            if curso.sigla==sigla:
                return curso
        return None
# Create your models here.
