# Generated by Django 2.0 on 2017-12-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password_hash', models.CharField(max_length=100)),
                ('date_registered', models.CharField(max_length=100)),
            ],
        ),
    ]