# Generated by Django 4.2.5 on 2023-09-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nmodel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title2', models.CharField(default='', max_length=40)),
                ('body2', models.CharField(default='', max_length=50)),
                ('status2', models.BooleanField(default=False)),
            ],
        ),
    ]
