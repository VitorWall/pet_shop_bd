# Generated by Django 3.2 on 2021-04-20 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pet_shop', '0002_alter_acomodacao_tamanho'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='sevico',
            new_name='servico',
        ),
    ]