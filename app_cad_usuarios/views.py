from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        if nome and idade:
            novo_usuario = Usuario()
            novo_usuario.nome = nome
            novo_usuario.idade = idade
            novo_usuario.save()
        

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
