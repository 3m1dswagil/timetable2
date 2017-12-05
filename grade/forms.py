# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Disciplina
from .models import Disciplina_ministrada, Disciplina_turma
from .models import Professor, Carga_horaria_disciplina
from .models import Turma
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

CARGA_HORARIA_CHOICES = (
    ('1', '1 aula'),
    ('2', '2 aulas'),
    ('3', '3 aulas'),
    ('4', '4 aulas'),
    ('5', '5 aulas'),
    ('6', '6 aulas'),
)

class Disciplina_form(forms.Form):
    codigo = forms.CharField(label='Código', max_length=20)
    nome = forms.CharField(label='Nome', max_length=100)
    # carga_horaria = forms.ChoiceField(choices=CARGA_HORARIA_CHOICES, widget=forms.RadioSelect())

    class Meta:
        widgets = {
            'codigo': TextInput(attrs={'class':'form-control','placeholder': 'teste'})
}


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



class Professor_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Matrícula', max_length=100)
    disciplinas = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Disciplina.objects.all())
    restricao_dia_semana = forms.ChoiceField(choices=RESTRICAO_DIA_CHOICES, widget=forms.RadioSelect())
    restricao_horario = forms.MultipleChoiceField(choices=RESTRICAO_HORA_CHOICES, widget=forms.CheckboxSelectMultiple())

class Disciplina_ministrada_form(forms.Form):
    codigo_disciplina = forms.CharField(label='Codigo', max_length=15)
    professor_disciplina = forms.ModelMultipleChoiceField(queryset=Disciplina_ministrada.objects.all())

class Turma_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    codigo = forms.CharField(label='Código', max_length=100)
    disciplina_ministrada = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Disciplina_ministrada.objects.all())
    # carga_horaria_disciplina = forms.ChoiceField(choices=CARGA_HORARIA_CHOICES)


class Disciplina_turma_form(forms.Form):
    turma = forms.ModelMultipleChoiceField(queryset=Turma.objects.all())
    disciplina_ministrada = forms.ModelMultipleChoiceField(queryset=Disciplina_ministrada.objects.all())
    # carga_horaria = forms.ChoiceField(choices=CARGA_HORARIA_CHOICES)

class Carga_horaria_disciplina_form(forms.Form):
    disciplina_ministrada = forms.ModelMultipleChoiceField(widget=forms.RadioSelect,queryset=Disciplina_ministrada.objects.all())
    carga_horaria = forms.ChoiceField(choices=CARGA_HORARIA_CHOICES)
