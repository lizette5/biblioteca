# Generated by Django 4.0.5 on 2022-11-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_alter_prestamo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
    ]
