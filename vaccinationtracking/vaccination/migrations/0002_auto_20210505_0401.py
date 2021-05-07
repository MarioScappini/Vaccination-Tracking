# Generated by Django 3.2 on 2021-05-05 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medic',
            name='id',
        ),
        migrations.AlterField(
            model_name='medic',
            name='medic_ssn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='vaccination.person'),
        ),
    ]