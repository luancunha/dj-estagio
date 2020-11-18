from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import thisAlunos, thisEstagio
from estagio.models import faculdades, cursos, profcoorest, alunos, estagio
from django.db import connection

def index(request):
    return render(request,'estagio/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Usúario ou Senha não está correto')
            return redirect('login')
    else:
        if request.user.is_active:
            return redirect('dashboard')
        else:
            return render(request,'estagio/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login')

def dashboard(request):
    return render(request,'estagio/dashboard/index.html')

def cad_alunos(request):
    curs = cursos.objects.all()

    if request.method == 'POST':
        Form = thisAlunos(request.POST)
        if Form.is_valid():
            Form.save()
            messages.error(request,'Usúario cadastrado com sucesso')
            return redirect('cad_alunos')
        else:
            messages.error(request,'Usúario não cadastrado')
            return redirect('cad_alunos')

    else:
        Form = thisAlunos()

    return render(request,'estagio/dashboard/cad_alunos.html', {'form':Form, 'curs':curs})

def cad_estagio(request):
    alu = alunos.objects.all()
    prof = profcoorest.objects.all()

    if request.method == 'POST':
        Form = thisEstagio(request.POST)
        if Form.is_valid():
            Form.save()
            messages.error(request,'Estágio cadastrado com sucesso')
            return redirect('cad_estagio')
        else:
            messages.error(request,'Estágio não cadastrado')
            return redirect('cad_estagio')

    else:
        Form = thisEstagio()

    return render(request,'estagio/dashboard/cad_estagio.html', {'form':Form, 'alu':alu, 'prof':prof})

def pesquisar(request):
    def sql():
        cursor = connection.cursor()
        cursor.execute("SELECT a.nome, a.matricula, c.nome FROM alunos as A INNER JOIN cursos as C ON a.curso=c.codigo INNER JOIN estagio as E ON a.matricula=e.aluno ORDER BY a.nome LIMIT 7;")
        row = cursor.fetchall()
        return row
    
    alu = sql()

    query = request.GET.get('matricula')

    def sql2(matricula):
        cursor = connection.cursor()
        cursor.execute("SELECT a.nome, a.matricula, c.nome FROM alunos as A INNER JOIN cursos as C ON a.curso=c.codigo INNER JOIN estagio as E ON a.matricula=e.aluno WHERE a.matricula=%s;", [matricula])
        row2 = cursor.fetchall()
        return row2

    if query != '' and query is not None:
        alu = sql2(query)

    context = {
        'alu': alu
    }
    return render(request, 'estagio/dashboard/pesquisar.html', context)

def detalhes(request, alu_id):
    try:
        est = estagio.objects.filter(aluno=alu_id)
        return render(request,'estagio/dashboard/detalhes.html', {'est': est,})
    except:
        return HttpResponse("Aluno não encontrado")