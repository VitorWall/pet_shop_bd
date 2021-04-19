# Generated by Django 3.2 on 2021-04-19 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acomodacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='número')),
                ('tamanho', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=70)),
                ('telefone', models.CharField(max_length=11)),
                ('vip', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField()),
                ('nome', models.CharField(max_length=70)),
                ('endereco', models.CharField(max_length=70, verbose_name='endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=70)),
                ('descricao', models.CharField(max_length=400, verbose_name='descrição')),
                ('duracao_media', models.DurationField(verbose_name='duração média')),
                ('unidades', models.ManyToManyField(through='sistema_pet_shop.Oferecimento', to='sistema_pet_shop.Unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='número')),
                ('equipamentos', models.CharField(max_length=100)),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('especie', models.CharField(max_length=70, verbose_name='espécie')),
                ('raca', models.CharField(max_length=20, verbose_name='raça')),
                ('sexo', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='oferecimento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.servico'),
        ),
        migrations.AddField(
            model_name='oferecimento',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.unidade'),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.IntegerField()),
                ('nome', models.CharField(max_length=70)),
                ('cargo', models.CharField(max_length=70)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='salário')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('aplicacao', models.CharField(max_length=200, verbose_name='aplicação')),
                ('quantidade', models.IntegerField()),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estadia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('acomodacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.acomodacao')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.pet')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='unidades',
            field=models.ManyToManyField(through='sistema_pet_shop.Cadastro', to='sistema_pet_shop.Unidade'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.cliente'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.unidade'),
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.funcionario')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.pet')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.sala')),
            ],
        ),
        migrations.AddField(
            model_name='acomodacao',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pet_shop.unidade'),
        ),
    ]
