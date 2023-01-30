from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "GET":
        vendedores = Users.objects.filter(cargo="V")
        return render(request, 'cadastrar_vendedor.html', {'vendedores':vendedores})
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)

        if user.exists():
           messages.add_message(request, messages.ERROR, 'E-mail já existente!')
           return redirect(reverse('cadastrar_vendedor'))

        user = Users.objects.create_user(username=email,
                                         email=email,
                                         password=senha,
                                         first_name=nome,
                                         last_name=sobrenome,
                                         cargo="V")
        messages.add_message(request, messages.SUCCESS, 'Vendedor cadastrado com sucesso!')
        return redirect(reverse('cadastrar_vendedor'))

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('add_produto'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            #return HttpResponse('Usuário inválido')
            messages.add_message(request, messages.ERROR, 'Usuário inválido')
            return redirect(reverse('login'))

        auth.login(request, user)
        #return HttpResponse('Usuário logado com sucesso!')
        return redirect(reverse('add_produto'))

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('excluir_vendedor')
def excluir_usuario(request, id):
    # BUSQUE ESSA INFO NO BANCO DE DADOS, SE NÃO EXISTIR RETORNE 404
    # SE EXISTIR ----> GUARDE NA VARIÁVEL
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    messages.add_message(request, messages.SUCCESS, 'Vendedor excluído com sucesso!')
    return redirect(reverse('cadastrar_vendedor'))
