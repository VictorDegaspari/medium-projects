from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['emails']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            return redirect('cadastro')

        if not email.strip():
            return redirect('cadastro')

        if senha != senha2:
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        print('Usuário criado com sucesso')
        return redirect('login')
    return render(request, 'usuarios/login.html')


def logout(request):
    pass


def dashboard(request):
    pass
