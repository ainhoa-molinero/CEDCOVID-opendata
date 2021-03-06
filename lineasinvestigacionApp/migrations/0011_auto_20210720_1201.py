# Generated by Django 3.2.5 on 2021-07-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0010_alter_archivo_url_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(max_length=255)),
                ('url_proyecto', models.URLField(max_length=255, null=True)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='lineainvestigacion',
            name='proyecto',
            field=models.ManyToManyField(blank=True, to='lineasinvestigacionApp.Proyecto'),
        ),
    ]
