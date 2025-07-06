from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    estado_origem = models.CharField(max_length=2)
    situacao = models.BooleanField(default=True)
    data_inclusao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    numero = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.numero} - {self.cliente.nome}"

class Servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='servicos')
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo} - {self.cliente.nome}"
