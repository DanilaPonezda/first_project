# Generated by Django 4.1.7 on 2023-03-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=33)),
                ('password', models.CharField(max_length=66)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
