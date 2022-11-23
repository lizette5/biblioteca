# Generated by Django 4.0.5 on 2022-11-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('dni', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.genero'),
        ),
    ]