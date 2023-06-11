from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def clientes(request):
    if request.method == "GET":
       # clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('tel')
        descricao = request.POST.get('descricao')

''' cliente = Cliente.objects.filter(cpf=cpf)

    if cliente.exists():
        return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'tel': telefone, 'descricao': descricao})

    if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
        return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'tel': telefone, 'descricao': descricao })

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf,
            telefone = telefone,
            descricao = descricao
        )

        cliente.save()

        return HttpResponse('Teste')       


def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    data = {'cliente': cliente_json, 'cliente_id': cliente_id}
    return JsonResponse(data)


@csrf_exempt

def update_cliente(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']
    telefone = body['tel']
    descricao = body['descricao']


    cliente = get_object_or_404(Cliente, id=id)
    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.telefone = telefone
        cliente.descricao = descricao
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf, 'tel': telefone, 'descricao': descricao })
    except:
        return JsonResponse({'status': '500'})
'''