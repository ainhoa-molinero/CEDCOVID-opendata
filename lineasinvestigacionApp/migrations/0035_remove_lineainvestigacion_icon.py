# Generated by Django 3.2.5 on 2021-09-30 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0034_alter_permiso_id_linea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineainvestigacion',
            name='icon',
        ),
    ]
