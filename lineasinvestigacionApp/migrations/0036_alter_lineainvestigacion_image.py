# Generated by Django 3.2.5 on 2022-01-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0035_remove_lineainvestigacion_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineainvestigacion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
