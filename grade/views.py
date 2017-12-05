# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Disciplina_form
from .forms import Professor_form, Carga_horaria_disciplina_form
from .forms import Turma_form, Disciplina_ministrada_form, Disciplina_turma_form
from django.views.generic import ListView
from grade.models import Disciplina, Professor, Turma, Disciplina_ministrada
from grade.models import Disciplina_turma, Carga_horaria_disciplina, Carga_horaria
from django.template.response import TemplateResponse
# Create your views here.

def disciplina_new(request):
    form = Disciplina_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            disciplina = Disciplina()
            disciplina.codigo = form.cleaned_data['codigo']
            disciplina.nome = form.cleaned_data['nome']
            # disciplina.carga_horaria = form.cleaned_data['carga_horaria']
            disciplina.save()
            return redirect("disciplina_list")
    return render(request, 'grade/cad_disc.html', {'form': form})

def professor_new(request):
    form = Professor_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            professor = Professor()
            professor.nome = form.cleaned_data['nome']
            professor.codigo = form.cleaned_data['codigo']
            disciplinas = form.cleaned_data['disciplinas']
            professor.restricao_horario = form.cleaned_data['restricao_horario']
            professor.restricao_dia_semana = form.cleaned_data['restricao_dia_semana']
            professor.save()
            for nome in disciplinas:

                disciplina_habilitada = Disciplina.objects.filter(nome=nome)[0:1].get()

                disciplina_ministrada = Disciplina_ministrada()
                disciplina_ministrada.professor = professor
                disciplina_ministrada.codigo = professor.codigo + disciplina_habilitada.codigo
                disciplina_ministrada.disciplina = disciplina_habilitada
                disciplina_ministrada.save()

            return redirect("professor_list")

    return render(request, 'grade/cad_prof.html', {'form': form})


# def turma_new(request):
#     form = Turma_form(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             turma = Turma()
#             turma.nome = form.cleaned_data['nome']
#             turma.codigo = form.cleaned_data['codigo']
#             disciplina_ministrada = form.cleaned_data['disciplina_ministrada']
#
#             turma.save()
#             for codigo_disciplina in disciplina_ministrada:
#                 disciplina_habilitada = Disciplina_ministrada.objects.filter(pk=codigo_disciplina.pk)[0:1].get()
#
#                     # for objeto in
#
#                 carga_horaria_disciplina = form.cleaned_data['carga_horaria']
#                 disciplina_turma = Disciplina_turma()
#                 disciplina_turma.turma = turma
#                 disciplina_turma.disciplina_ministrada=disciplina_habilitada
#                 disciplina_turma.carga_horaria = carga_horaria_disciplina
#
#                 disciplina_turma.save()
#
#
#             return redirect("turma_list")
#     return render(request, 'grade/cad_turma.html', {'form': form})

def turma_new(request):
    form = Turma_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            turma = Turma()
            turma.nome = form.cleaned_data['nome']
            turma.codigo = form.cleaned_data['codigo']

            turma.save()
            disciplina_ministrada = form.cleaned_data['disciplina_ministrada']
            for codigo_disciplina in disciplina_ministrada:
                disciplina_habilitada = Disciplina_ministrada.objects.filter(pk=codigo_disciplina.pk)[0:1].get()

                # carga_horaria_disciplina = form.cleaned_data['carga_horaria']
                disciplina_turma = Disciplina_turma()
                # disciplina_turma.carga_horaria_disciplina = carga_horaria_disciplina
                disciplina_turma.turma = turma
                disciplina_turma.disciplina_ministrada=disciplina_habilitada

                disciplina_turma.save()

            return redirect("carga_horaria")
    return render(request, 'grade/cad_turma.html', {'form': form})


def carga_horaria(request):
    form2 = Carga_horaria_disciplina_form(request.POST or None)
    if request.method == 'POST':
        if form2.is_valid():
            for obj in disciplina_turma:
                disciplina_habilitada2 = Disciplina_turma.objects.filter(pk=codigo_disciplina.pk)[0:1].get()

                carga_horaria = form.cleaned_data['carga_horaria']
                for objeto in  disciplina_habilitada2:

                    carga_horaria_disciplina = Carga_horaria_disciplina()
                    carga_horaria_disciplina.disciplina_turma.disciplina_turma = disciplina_habilitada2.turma
                    carga_horaria_disciplina.disciplina_turma.disciplina_ministrada = disciplina_habilitada2.disciplina_ministrada
                    carga_horaria_disciplina.carga_horaria = carga_horaria

                    carga_horaria_disciplina.save()

            return redirect("turma_list")
    return render(request, 'grade/cad_carga_horaria.html', {'form2':form2})

# def disciplina_ministrada_new(request):
#     form = Disciplina_ministrada(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             disciplina_ministrada = form.cleaned_data['disciplina_ministrada']
#             disciplina_ministrada.save()


################################################################################
def enum_carga_horaria(request):
    dados_enum_carga_horaria = Carga_horaria.objects.all()
    return TemplateResponse(request, 'grade/cad_carga_horaria.html', {'dados_enum_carga_horaria': dados_enum_carga_horariat})

def carga_horaria_list(request):
    dados_carga_horaria_list = Disciplina_turma.objects.all()
    return TemplateResponse(request, 'grade/cad_carga_horaria.html', {'dados_carga_horaria_list': dados_carga_horaria_list})

def grade_list(request):
    dados_grade_list = Disciplina_turma.objects.all()
    return render(request, 'grade/grade.html', {'dados_grade_list': dados_grade_list})

def disciplina_list(request):
    dados_disciplina_list = Disciplina.objects.all()
    return TemplateResponse(request, 'grade/lista_disc.html', {'dados_disciplina_list': dados_disciplina_list})

def professor_list(request):
    dados_professor_list = Disciplina_ministrada.objects.all()
    return TemplateResponse(request, 'grade/lista_prof.html', {'dados_professor_list': dados_professor_list})

def turma_list(request):
    dados_turma_list = Turma.objects.all()
    return TemplateResponse(request, 'grade/lista_turma.html', {'dados_turma_list': dados_turma_list})

def pagina_inicial(request):
    return render(request, 'grade/pag_inicial.html')
