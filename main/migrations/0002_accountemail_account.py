# Generated by Django 4.1.7 on 2023-03-19 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=30)),
                ('port', models.SmallIntegerField()),
                ('password', models.CharField(max_length=66)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=66)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.accountemail')),
            ],
        ),
    ]
