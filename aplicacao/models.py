from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=12)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)

    def _str_(self) -> str:
        return self.nome
    
'''class Servico (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL)
    tipo = models.CharField(max_length=15)
    contratos = models.IntegerField(default=0)
'''

