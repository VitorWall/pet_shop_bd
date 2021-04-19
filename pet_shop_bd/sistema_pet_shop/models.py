from django.db import models

class Unidade(models.Model):
    cep = models.IntegerField()#, primary_key=True)
    nome = models.CharField(max_length=70)
    endereco = models.CharField('endereço', max_length=70)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    CPF = models.CharField(max_length=11)#, primary_key=True)
    nome = models.CharField(max_length=70)
    telefone = models.CharField(max_length=11)
    vip = models.BooleanField()

    unidades = models.ManyToManyField(
        Unidade,
        through='Cadastro',
        through_fields=('cliente', 'unidade'),
    )

    def __str__(self):
        return self.nome
        
class Pet(models.Model):
    nome = models.CharField(max_length=70)
    especie = models.CharField('espécie', max_length=70)
    raca = models.CharField('raça', max_length=20)
    sexo = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    CPF = models.IntegerField()#, primary_key=True)
    nome = models.CharField(max_length=70)
    cargo = models.CharField(max_length=70)
    salario = models.DecimalField('salário', decimal_places=2, max_digits=10)
    unidade =  models.ForeignKey(Unidade, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Servico(models.Model):
    tipo = models.CharField(max_length=70)
    descricao = models.CharField('descrição', max_length=400)
    duracao_media = models.DurationField('duração média')
    unidades = models.ManyToManyField(
        Unidade,
        through='Oferecimento',
        through_fields=('servico', 'unidade'),
    )

    def __str__(self):
        return self.service_type


class Estoque(models.Model):
    nome = models.CharField(max_length=70)#, primary_key=True)
    aplicacao = models.CharField('aplicação', max_length=200)
    quantidade = models.IntegerField()
    unidade =  models.ForeignKey(Unidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Acomodacao(models.Model):
    numero = models.IntegerField('número')#, primary_key=True)
    tamanho = models.IntegerField()
    unidade =  models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)

class Sala(models.Model):
    numero = models.IntegerField('número')#, primary_key=True)
    equipamentos = models.CharField(max_length=100)
    unidade =  models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)
    

# Relacionamentos
class Agendamento(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

class Estadia(models.Model):
    data_inicial = models.DateField()
    data_final = models.DateField()
    acomodacao =  models.ForeignKey(Acomodacao, on_delete=models.CASCADE)
    pet =  models.ForeignKey(Pet, on_delete=models.CASCADE)


class Oferecimento(models.Model):
    unidade =  models.ForeignKey(Unidade, on_delete=models.CASCADE)
    servico =  models.ForeignKey(Servico, on_delete=models.CASCADE)

class Cadastro(models.Model):
    unidade =  models.ForeignKey(Unidade, on_delete=models.CASCADE)
    cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)
