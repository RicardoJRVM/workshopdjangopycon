# Generated by Django 2.2.5 on 2019-09-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('libro_id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
