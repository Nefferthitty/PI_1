# Generated by Django 3.2.8 on 2021-10-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vereador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_vereador', models.CharField(max_length=200)),
                ('nome_assessor', models.CharField(max_length=200)),
            ],
        ),
    ]
