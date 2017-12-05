# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

RESTRICAO_DIA_CHOICES = (
    ('0', 'Nenhuma'),
    ('2', 'Segunda'),
    ('3', 'Terça'),
    ('4', 'Quarta'),
    ('5', 'Quinta'),
    ('6', 'Sexta'),
)

RESTRICAO_HORA_CHOICES = (
    ('0', 'Nenhuma'),
    ('1', 'Primeira'),
    ('2', 'Segunda'),
    ('3', 'Terceira'),
    ('4', 'Quarta'),
    ('5', 'Quinta'),
    ('6', 'Sexta'),

)

TURNO_CHOICES = (
    ('0', 'Matutino'),
    ('1', 'Vespertino'),
    ('2', 'Noturno'),

)

CARGA_HORARIA_CHOICES = (
    ('1', '1 aula'),
    ('2', '2 aulas'),
    ('3', '3 aulas'),
    ('4', '4 aulas'),
    ('5', '5 aulas'),
    ('6', '6 aulas'),
)

class Carga_horaria(models.Model):
    primeira = models.CharField(max_length=20)
    segunda = models.CharField(max_length=20)
    terceira = models.CharField(max_length=20, choices=CARGA_HORARIA_CHOICES)
# -*- coding: utf-8 -*-
class Escola(models.Model):
    nome = models.CharField(max_length=70)
# -*- coding: utf-8 -*-
class Coordenador(models.Model):
    nome = models.CharField(max_length=70)
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)
    escola = models.ForeignKey('Escola')
# -*- coding: utf-8 -*-
class Professor(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    nome = models.CharField(max_length=70)
    codigo = models.CharField(max_length=12)
    restricao_dia_semana =  models.CharField(max_length=5, choices=RESTRICAO_DIA_CHOICES)
    restricao_horario =  models.TextField(max_length=8, choices=RESTRICAO_HORA_CHOICES)

    def __str__(self):
            return str(self.nome)

# -*- coding: utf-8 -*-
class Disciplina(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    # carga_horaria = models.TextField(max_length=1, choices=CARGA_HORARIA_CHOICES)

    def __str__(self):
         return str(self.nome)

    def __unicode__(self):
        return u'{f}'.format(f=self.nome)

# -*- coding: utf-8 -*-
class Disciplina_ministrada(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    codigo_disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)

    def __str__(self):
          return ('%s - %s' % (self.disciplina, self.professor))

# -*- coding: utf-8 -*-
class Turma(models.Model):
    nome = models.CharField(max_length=20)
    codigo = models.CharField(max_length=12)
    def __str__(self):
         return str(self.nome)

class Disciplina_turma(models.Model):
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)
    disciplina_ministrada = models.ForeignKey('Disciplina_ministrada', on_delete=models.CASCADE)
    # carga_horaria = models.TextField(max_length=1, choices=CARGA_HORARIA_CHOICES)

class Carga_horaria_disciplina(models.Model):
    disciplina_turma = models.ForeignKey('Disciplina_ministrada', on_delete=models.CASCADE)
    carga_horaria = models.TextField(max_length=1, choices=CARGA_HORARIA_CHOICES)

# Create your models here.
