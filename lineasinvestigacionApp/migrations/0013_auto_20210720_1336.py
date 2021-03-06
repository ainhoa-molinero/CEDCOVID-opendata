# Generated by Django 3.2.5 on 2021-07-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0012_auto_20210720_1307'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produccion',
            new_name='Producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='id_produccion',
            new_name='id_producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_produccion',
            new_name='nombre_producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='url_produccion',
            new_name='url_producto',
        ),
        migrations.RemoveField(
            model_name='lineainvestigacion',
            name='produccion',
        ),
        migrations.AddField(
            model_name='lineainvestigacion',
            name='producto',
            field=models.ManyToManyField(blank=True, to='lineasinvestigacionApp.Producto'),
        ),
    ]
