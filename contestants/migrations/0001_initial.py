# Generated by Django 4.0.4 on 2022-05-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=15)),
                ('verified', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]