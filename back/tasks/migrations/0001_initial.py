# Generated by Django 2.0 on 2018-04-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('day', models.DateField()),
                ('to_time', models.DateTimeField()),
            ],
        ),
    ]
