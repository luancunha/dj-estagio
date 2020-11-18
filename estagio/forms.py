from django import forms
from .models import alunos, estagio

class thisAlunos(forms.ModelForm):
    class Meta:
        model = alunos
        fields = ['matricula', 'nome', 'sexo', 'datanasc', 'periodo', 'curso']

class thisEstagio(forms.ModelForm):
    class Meta:
        model = estagio
        fields = ['aluno', 'profest', 'remunerado', 'valor', 'empresa', 'cargahr', 'descr_est', 'resp_est']