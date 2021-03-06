# Generated by Django 3.2.5 on 2021-08-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0024_rename_categoria_categoria_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.AlterField(
            model_name='archivo',
            name='categoria_archivo',
            field=models.ManyToManyField(blank=True, choices=[('BD', 'Bases de datos'), ('E', 'Estadística'), ('EP', 'Ensamblaje de proteínas')], max_length=500, to='lineasinvestigacionApp.Categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
