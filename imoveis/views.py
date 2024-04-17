from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from imoveis.forms import ImovelForm, PesquisaForm
from imoveis.models import Imovel, Usuario
from django.contrib.auth import login, logout


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cadastrar_imovel')  
    else:
        form = AuthenticationForm()

    return render(request, 'imoveis/registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  


def sobre(request):
    user = Usuario

    return render(request, 'imoveis/sobre.html', {'user': user})


def cadastrar_imovel(request):
    form = ImovelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_imoveis')
    return render(request, 'imoveis/cadastrar_imovel.html', {'form': form})


def lista_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imoveis/resultados_pesquisa.html', {'resultados_pesquisa': imoveis})


def excluir_imovel(request, imovel_id):
    imovel = Imovel.objects.get(id=imovel_id)
    imovel.delete()
    return redirect('lista_imoveis')
