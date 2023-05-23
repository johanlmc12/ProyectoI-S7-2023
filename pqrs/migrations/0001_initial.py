# Generated by Django 4.2 on 2023-05-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabla_modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('frase', models.CharField(max_length=255)),
                ('prediccion', models.FloatField()),
                ('asunto', models.CharField(max_length=255)),
                ('tipo_solicitud', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
