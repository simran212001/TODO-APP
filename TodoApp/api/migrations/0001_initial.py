# Generated by Django 4.0.1 on 2022-01-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=30)),
                ('task_desc', models.TextField()),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
