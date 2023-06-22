# Generated by Django 4.2.2 on 2023-06-22 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.IntegerField()),
                ('employee_first_name', models.CharField(max_length=30)),
                ('employee_last_name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=100)),
                ('supervisor_number', models.IntegerField()),
                ('hire_date', models.DateField(null=True)),
                ('pto_balance', models.DecimalField(decimal_places=4, max_digits=7)),
                ('active', models.BooleanField()),
                ('isSupervisor', models.BooleanField()),
                ('isAdmin', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]