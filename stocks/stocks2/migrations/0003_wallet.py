# Generated by Django 3.2.6 on 2021-08-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks2', '0002_credentials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=36)),
            ],
        ),
    ]
