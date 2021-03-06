# Generated by Django 3.2 on 2021-05-05 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_ssn', models.IntegerField(primary_key=True, serialize=False)),
                ('person_fname', models.CharField(max_length=20)),
                ('person_lname', models.CharField(max_length=50)),
                ('person_email', models.CharField(max_length=70)),
                ('person_phone', models.IntegerField()),
                ('person_addr', models.CharField(max_length=100)),
                ('person_priority', models.IntegerField()),
                ('person_is_medic', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.IntegerField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=30)),
                ('place_addr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('vaccine_name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('vaccine_stock', models.IntegerField()),
                ('vaccine_no_of_shots', models.IntegerField()),
                ('vaccine_effectivity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_wants_vaccine', models.BooleanField(default=False)),
                ('patient_was_vaccinated', models.BooleanField(default=False)),
                ('patient_ssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.person')),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medic_type', models.CharField(max_length=25)),
                ('medic_was_vaccinated', models.BooleanField(default=False)),
                ('medic_ssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.person')),
            ],
        ),
    ]
