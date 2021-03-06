# Generated by Django 4.0.4 on 2022-06-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('conservacion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ingrediente_uno', models.CharField(max_length=40)),
                ('ingrediente_dos', models.CharField(max_length=40)),
                ('ingrediente_tres', models.CharField(max_length=40)),
                ('tiempo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('usuario', models.CharField(max_length=8)),
                ('contraseña', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]
