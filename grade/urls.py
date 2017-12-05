from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^novadisciplina', views.disciplina_new, name='disciplina_new'),
    url(r'^disciplinas', views.disciplina_list, name='disciplina_list'),
    url(r'^novoprofessor', views.professor_new, name='professor_new'),
    url(r'^professores', views.professor_list, name='professor_list'),
    url(r'^novaturma', views.turma_new, name='turma_new'),
    url(r'^cargahoraria', views.carga_horaria, name='carga_horaria'),
    url(r'^turma', views.turma_list, name='turma_list'),
    url(r'^grade', views.grade_list, name='grade_list'),
    url(r'^$', views.pagina_inicial, name='pagina_inicial'),

]
