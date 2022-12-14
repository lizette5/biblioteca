# Generated by Django 4.0.5 on 2022-11-23 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0004_alter_genero_id_alter_libro_id_alter_prestamo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='anio',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Academico.genero'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='id_libro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Academico.libro'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Academico.usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellidos',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
